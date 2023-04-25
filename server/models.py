from sqlalchemy_serializer import SerializerMixin

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    