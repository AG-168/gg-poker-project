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
        # for i in range(2):
        #     user = User(
        #         username=fake.user_name(),
        #         email=fake.email(),
        #     )
        #     user.set_password('password')
        #     db.session.add(user)
        #     db.session.commit()

        user = User(
            name='test',
            email='test@email.com',
        )
        # user.set_password('password')
        db.session.add(user)
        db.session.commit()

        review1 = Review(
            review='This is a test review',
            user_id=1,
            skatepark_id=1
        )
        review2 = Review(
            review='This is another test review',
            user_id=1,
            skatepark_id=1
        )

        db.session.add_all([review1, review2])
        db.session.commit()
    

        
        skatepark1 = Skatepark(
            name='Bronx Skate Park',
            address='Southern Blvd,Webster,Burke Aves,Bronx Pk E,180 St',
            borough ='Bronx',
            hours='Closes at dusk'
        )

        skatepark2 = Skatepark(
            name='Bruckner Skate Park',
            address='Brinsmade Ave. bet. Cross Bronx Ser. Rd. and Swinton Ave.',
            borough='Bronx',
            hours='Dawn to dusk.'
        )

        skatepark3 = Skatepark(
            name='Mullaly Skate Park',
            address='East 164th Street and Jerome & River avenues',
            borough='Bronx',
            hours='During the school year only. Weekdays: 3:00 p.m. to dusk Weekends: 1:00 p.m. to dusk'
        )

        skatepark4 = Skatepark(
            name='Playground 52 LII Skate Park',
            address='Kelly St. & Avenue St. John',
            borough='Bronx',
            hours='7:00 a.m. - 9:00 p.m. (March 2 - October 31); 7:00 a.m. - 6:00 p.m. (November 1 - March 1)'
        )

        skatepark5 = Skatepark(
            name='Playground One Thirty Four CXXXIV Skate Park',
            address="St. Ann's Pl & Bruckner Blvd",
            borough='Bronx',
            hours='Dawn to dusk.'
        )

        skatepark6 = Skatepark(
            name='River Avenue Skate Park',
            address="East 157th Street and River Avenue",
            borough='Bronx',
            hours='6:00 a.m. to 10:00 p.m.'
        )

        skatepark7 = Skatepark(
            name='Van Cortlandt Skate Park',
            address="Van Cortlandt Stadium, Broadway & Van Cortlandt Park S",
            borough='Bronx',
            hours='6:00 a.m. to 10:00 p.m.'
        )

        skatepark8 = Skatepark(
            name='Williamsbridge Oval Skate Park',
            address="Holt Place and Reservoir Oval",
            borough='Bronx',
            hours='6:00 a.m. to 10:00 p.m.'
        )

        skatepark9 = Skatepark(
            name='Betsy Head Skate Park',
            address="Blake Ave & Bristol St",
            borough='Brooklyn',
            hours='6:00 a.m. - 1:00 a.m.'
        )

        skatepark10 = Skatepark(
            name='Brower Park Skate Park',
            address="St. Mark's Ave., Park Pl. bet. Brooklyn Ave. and Kingston Ave.",
            borough='Brooklyn',
            hours='Dawn to dusk'
        )

        skatepark11 = Skatepark(
            name='Canarsie Skate Park',
            address="Belt Pkwy, Seaview Ave Btw: Paerdegat Basin, E 93 S, E 102 St, Fresh Creek Basin",
            borough='Brooklyn',
            hours='6:00 a.m. to 9:00 p.m.'
        )

        skatepark12 = Skatepark(
            name='City Line Park',
            address="Belt Pkwy, Seaview Ave Btw: Paerdegat Basin, E 93 S, E 102 St, Fresh Creek Basin",
            borough='Brooklyn',
            hours='6:00 a.m. to 9:00 p.m.'
        )

        skatepark13 = Skatepark(
            name='Cooper Park',
            address="At Sharon Street, between Morgan Avenue and Olive Street",
            borough='Brooklyn',
            hours='6:00 a.m. to 1:00 a.m.'
        )
        
        skatepark14 = Skatepark(
            name='Golconda Skate Park',
            address="Nassau St. & Gold St.",
            borough='Brooklyn',
            hours='Dawn to dusk.'
        )

        skatepark15 = Skatepark(
            name='Martinez Playground Skate Park',
            address="Scholes St. bet. Manhattan Ave. and Graham Ave.",
            borough='Brooklyn',
            hours='Dawn to dusk.'
        )
        
        skatepark16 = Skatepark(
            name='McCarren Skate Park',
            address="McCarren Skate Park is located behind McCarren Pool",
            borough='Brooklyn',
            hours='Closes at dusk.'
        )

        skatepark17 = Skatepark(
            name='Millennium Skate Park',
            address="Colonial Road between 68th Street and Wakeman Place in Owl's Head Park",
            borough='Brooklyn',
            hours='Daily, 11:00 a.m. to 7:00 p.m.'
        )

        skatepark18 = Skatepark(
            name='Robert Venable Skate Park',
            address="Belmont Ave., Sutter Ave., Sheridan Ave. and Grant Ave.",
            borough='Brooklyn',
            hours='8:00 a.m. to dusk'
        )

        skatepark19 = Skatepark(
            name='Rudd Skate Park',
            address="Aberdeen St at Bushwick Ave",
            borough='Brooklyn',
            hours='6:00 a.m. - 9:00 p.m.'
        )

        skatepark20 = Skatepark(
            name='Seba Playground Skate Park',
            address="Near Gerritsen Avenue and Seba Avenue",
            borough='Brooklyn',
            hours='Dawn to dusk'
        )

        skatepark21 = Skatepark(
            name='Sgt. William Dougherty Skate Park',
            address="Vandervoort Ave. between Cherry St. & Anthony St.",
            borough='Brooklyn',
            hours='6:00 a.m. - 9:00 p.m.'
        )

        skatepark22 = Skatepark(
            name="St. Mary's Skate Park",
            address="Smith St. & Nelson St.",
            borough='Brooklyn',
            hours='6:00 a.m. - 9:00 p.m.'
        )

        skatepark23 = Skatepark(
            name="Washington Park Skate Park",
            address="5th street between 4th and 5th avenues",
            borough='Brooklyn',
            hours='Dawn to dusk'
        )

        skatepark24 = Skatepark(
            name="Andy Kessler Skate Park",
            address="Riverside Park near 108th Street and Riverside Drive, on the lower level",
            borough='Manhattan',
            hours='6:00 a.m. to 1:00 a.m.'
        )

        skatepark25 = Skatepark(
            name="Coleman Playground",
            address="Cherry Street, Market Street, Monroe Street & Pike Street",
            borough='Manhattan',
            hours='Dawn to dusk'
        )

        skatepark26 = Skatepark(
            name="Highbridge Skate Park",
            address="W 155 St and Dyckman St, Edgecombe Av & Amsterdam Av",
            borough='Manhattan',
            hours='Dawn to dusk'
        )

        skatepark27 = Skatepark(
            name="Thomas Jefferson Park Skate Park",
            address="East 114th Street and the FDR Drive, near the basketball courts",
            borough='Manhattan',
            hours='7:00 a.m. to 10:00 p.m.'
        )

        skatepark28 = Skatepark(
            name="Astoria Skate Park",
            address="19 St. bet. Astoria Park S. and Ditmars Blvd.",
            borough='Queens',
            hours='Dawn to dusk'
        )

        skatepark29 = Skatepark(
            name="Bayswater Park",
            address="Dwight Ave., Seagirt Blvd. bet. Beach 38 St. and Bay 32 St.",
            borough='Queens',
            hours='Dawn to dusk'
        )

        skatepark30 = Skatepark(
            name="Far Rockaway Skate Park",
            address="Beach 11th Street off Seagirt Blvd, near the Rockaway Beach Promenade",
            borough='Queens',
            hours='Dawn to dusk'
        )

        skatepark31 = Skatepark(
            name="Flushing Meadows Corona Skate Park",
            address="Grand Central Pkwy, Van Wyck Exwy",
            borough='Queens',
            hours='Dawn to dusk'
        )

        skatepark32 = Skatepark(
            name="Forest Park Skate Park",
            address="Forest Park Woodhaven Blvd &, Myrtle Ave, 11421",
            borough='Queens',
            hours='Dawn to dusk'
        )

        skatepark33 = Skatepark(
            name="Helen Marshall Playground",
            address="100 St & 24th Ave, East Elmhurst, NY 11369",
            borough='Queens',
            hours='Dawn to dusk'
        )

        skatepark34 = Skatepark(
            name="Laurelton Skate Park",
            address="137th Ave &, Brookville Blvd, 11422",
            borough='Queens',
            hours='Dawn to dusk'
        )

        skatepark35 = Skatepark(
            name="London Planetree Skate Park",
            address="London Planetree Playground 89th St. &, Atlantic Ave, Jamaica, NY 11416",
            borough='Queens',
            hours='6:00 a.m. to 9:00 p.m.'
        )

        skatepark36 = Skatepark(
            name="Rockaway Skate Park",
            address="Shore Front Parkway at 91st Street (just off the boardwalk)",
            borough='Queens',
            hours='Currently closed for repairs.'
        )

        skatepark37 = Skatepark(
            name="Ben Soto Skate Park",
            address="Midland Beach Playground off of Father Capodanno Boulevard",
            borough='Staten Island',
            hours='Dawn to dusk.'
        )

        skatepark38 = Skatepark(
            name="Faber Skate Park",
            address="2175 Richmond Terrace",
            borough='Staten Island',
            hours='Dawn to dusk.'
        )

        db.session.add_all([skatepark1, skatepark2, skatepark3, skatepark4, skatepark5, skatepark6, skatepark7, skatepark8, skatepark9, skatepark10, skatepark11, skatepark12, skatepark13, skatepark14, skatepark15, skatepark16, skatepark17, skatepark18, skatepark19, skatepark20, skatepark21, skatepark22, skatepark23, skatepark24, skatepark25, skatepark26, skatepark27, skatepark28, skatepark29, skatepark30, skatepark31, skatepark32, skatepark33, skatepark34, skatepark35, skatepark36, skatepark37, skatepark38])
        db.session.commit()


