"""CRUD operations"""

from model import db, connect_to_db, User, Itinerary, Entry, PlaceType, EntryType

def create_user(username, email, password, fname=None, lname=None):
    """Create and return a new user"""

    new_user = User(username=username,
                email=email,
                password=password,
                fname=fname,
                lname=lname)
    
    db.session.add(new_user)
    db.session.commit()

    return new_user


def create_itinerary(user, name, start_date, end_date):
    """Create and return a new itinerary"""

    new_itinerary = Itinerary(
                            user=user,
                            name=name,
                            start_date=start_date,
                            end_date=end_date,
                            )
    
    db.session.add(new_itinerary)
    db.session.commit()

    return new_itinerary


def create_entry(itinerary, name, description, url, image, comment, location, trip_day, complete=False):
    """Create and return a new entry"""

    new_entry = Entry(
                    itinerary=itinerary,
                    name=name,
                    description=description,
                    url=url,
                    image=image,
                    comment=comment,
                    location=location,
                    trip_day=trip_day,
                    complete=complete
    )

    db.session.add(new_entry)
    db.session.commit()

    return new_entry


def create_new_type(place_type):
    """Create and return a new place type"""

    new_type = PlaceType(place_type=place_type)

    db.session.add(new_type)
    db.session.commit()

    return new_type


def create_new_entry_type(place_type, entry):
    """Create and return a new entry type"""

    new_entry_type = EntryType(place_type_id=place_type, entry_id=entry)

    db.session.add(new_entry_type)
    db.session.commit()

    return new_entry_type




if __name__ == '__main__':
    from server import app
    connect_to_db(app)