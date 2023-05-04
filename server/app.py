#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, jsonify, session, abort
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, Skatepark, Review

app.secret_key = b'\xe2f\x02\xceW\xbc/<\x8b\xb3\xe9\x15\x03\x18\xd5I'

class SkateparkList(Resource):
    def get(self):
        skateparks = Skatepark.query.all()
        skateparks_list = [skatepark.to_dict() for skatepark in skateparks]
        return make_response(skateparks_list, 200)

api.add_resource(SkateparkList, '/api/skateparks')

class ReviewById(Resource):
    def get(self, id):
        reviews = Review.query.filter(id == Review.skatepark_id).all()
        reviews_list = [review.to_dict() for review in reviews]
        return make_response(reviews_list, 200)
    
api.add_resource(ReviewById, '/api/reviews/<int:id>')

class Users(Resource):
    def post(self):
        form_json = request.get_json()
        new_user = User(
            name=form_json['name'],
            email=form_json['email']
        )
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        # import ipdb; ipdb.set_trace()
        response = make_response(
            new_user.to_dict(),
            201
        )
        return response
    
api.add_resource(Users, '/users')

class Login(Resource):
    def post(self):
        user = User.query.filter_by(name=request.get_json()['name']).first()
        session['user_id'] = user.id
        response = make_response(
            user.to_dict(),
            200
        )
        return response

api.add_resource(Login, '/login')

class AuthorizedSession(Resource):
    def get(self):
        user = User.query.filter_by(id=session.get('user_id')).first()
        if user:
            response = make_response(
                user.to_dict(),
                200
            )
            return response
        else:
            abort(401, "Unauthorized")
api.add_resource(AuthorizedSession, '/authorized')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None 
        response = make_response('',204)
        return response
api.add_resource(Logout, '/logout')




if __name__ == '__main__':
    app.run(port=5555, debug=True)
