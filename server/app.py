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

# Views go here!


if __name__ == '__main__':
    app.run(port=5555, debug=True)
