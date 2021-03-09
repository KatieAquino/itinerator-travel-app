"""Script to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime, date

from model import *
from crud import create_user
import server

os.system('dropdb testdb')
os.system('createdb testdb')

connect_to_db(server.app)
db.create_all()


mickey_mouse = create_user( username = 'mickeymouse',
                            email = 'mmouse@test.com',
                            password = '123password',
                            fname = 'Mickey',
                            lname = 'Mouse')

minnie_mouse = create_user(    username = 'minniemouse',
                        email = 'dotsandbows@test.com',
                        password = '456password',
                        fname = 'Minnie',
                        lname = 'Mouse'
                        )

donald_duck = create_user(     username = 'donaldduck',
                        email = 'dduck@test.com',
                        password = '789password',
                        fname = 'Donald',
                        lname = 'Duck'
                        )

daisy_duck = create_user(      username = 'daisyduck',
                        email = 'daisybow@test.com',
                        password = 'donaldstopnow',
                        fname = 'Daisy',
                        lname = 'Duck'
                        )

db_users = [mickey_mouse, minnie_mouse, donald_duck, daisy_duck]

for person in db_users:
    db.session.add(person)

db.session.commit()
print('*' * 50)
print('Users successfully added!')
print('*' * 50)

with open('data/itineraries.json') as o:
    itinerary_data = json.loads(o.read())

itineraries_in_db = []

for plan in itinerary_data:
    name = (plan['name'])
    start_date = datetime.strptime(plan['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(plan['end_date'], '%Y-%m-%d')
    random_user = choice(db_users)

    plan = Itinerary(user_id=random_user.id, 
                    name=name, 
                    start_date=start_date, 
                    end_date=end_date)

    itineraries_in_db.append(plan)
    db.session.add(plan)

db.session.commit()
print('*' * 50)
print('Itineraries successfully added!')
print('*' * 50)


with open('data/entries.json') as f:
    entry_data = json.loads(f.read())

entries_in_db = []

for entry_object in entry_data:
    name, description, url, image, comment, location, trip_day = (
                                                                entry_object['name'],
                                                                entry_object['description'],
                                                                entry_object['url'],
                                                                entry_object['image'],
                                                                entry_object['comment'],
                                                                entry_object['location'],
                                                                entry_object['trip_day']
    )

    random_itinerary = choice(itineraries_in_db)

    entry_object = Entry(
                            name=name,
                            description=description,
                            url=url,
                            image=image,
                            comment=comment,
                            location=location,
                            trip_day=trip_day,
                            itinerary_id=random_itinerary.id,
                            complete=False
                            )
    
    entries_in_db.append(entry_object)
    db.session.add(entry_object)

db.session.commit()
print('*' * 50)
print('Entries successfully added!')
print('*' * 50)


option_types = ['historic', 'museum', 'amusement park', 'beach',]
options_in_db = []

for item in option_types:
    item = PlaceType(place_type=item)
    options_in_db.append(item)

    db.session.add(item)

db.session.commit()
print('*' * 50)
print('PlaceTypes successfully added!')
print('*' * 50)

for item in entries_in_db:
    random_type = choice(options_in_db)
    random_entry = choice(entries_in_db)
    
    entry_type = EntryType(place_type_id=random_type.id,
                            entry_id=random_entry.id)
    
    db.session.add(entry_type)

db.session.commit()
print('*' * 50)
print('EntryTypes successfully added!')
print('*' * 50)
