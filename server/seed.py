#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Skatepark, Review

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        print("Dropping database...")

        db.drop_all()
        db.session.commit()

        print("Creating database...")
        db.create_all()
        db.session.commit()

        
        print("Starting seed...")
        # Seed code goes here!
        for i in range(2):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
            )
            user.set_password('password')
            db.session.add(user)
            db.session.commit()

        
        skatepark1 = Skatepark(
            name='Bronx Skate Park',
            address='Southern Blvd,Webster,Burke Aves,Bronx Pk E,180 St',
            city='New York City',
            hours='Closes at dusk'
        )

