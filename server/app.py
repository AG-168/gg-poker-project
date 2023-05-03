#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, jsonify, session
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, Skatepark, Review

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




if __name__ == '__main__':
    app.run(port=5555, debug=True)
