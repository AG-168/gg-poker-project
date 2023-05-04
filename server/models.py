from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-reviews.user', '-reviews.skatepark')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)

    _password_hash = db.Column(db.String(128))
    

    reviews = db.relationship('Review', back_populates='user')

    @hybrid_property
    def password_hash(self):
        return self._password_hash


    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

 
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
  
    def __repr__(self):
        return f'USER: ID: {self.id}, Name {self.name}, Email: {self.email}'

    

    
class Skatepark(db.Model, SerializerMixin):
    __tablename__ = 'skateparks'

    serialize_rules = ('-reviews.user', '-reviews.skatepark')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    borough = db.Column(db.String, nullable=False)
    hours = db.Column(db.String)

    reviews = db.relationship('Review', back_populates='skatepark')

    def __repr__(self):
        return f'<Skatepark {self.name}>'
    
    
class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    serialize_rules = ('-user.reviews', '-skatepark.reviews')

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    skatepark_id = db.Column(db.Integer, db.ForeignKey('skateparks.id'))

    user = db.relationship('User', back_populates='reviews')
    skatepark = db.relationship('Skatepark', back_populates='reviews')

    def __repr__(self):
        return f'<Review {self.review}>'
    
