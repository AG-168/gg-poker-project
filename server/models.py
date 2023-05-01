from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-reviews.user', '-reviews.skatepark')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    reviews = db.relationship('Review', back_populates='user')

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    

    def __repr__(self):
        return f'<User {self.username}>'   
    

    
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
    
