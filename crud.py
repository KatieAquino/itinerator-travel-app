"""CRUD operations"""

from model import db, connect_to_db, User, Itinerary, Entry, PlaceType, EntryType

def create_user(username, email, password, fname=None, lname=None):
    """Create and return a new user"""

    new_user = User(
                    username=username,
                    email=email,
                    fname=fname,
                    lname=lname)
    
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return new_user


def find_user_by_email(email):
    """Find user by email"""

    return User.query.filter(User.email == email).first()


def find_itinerary_by_user_id(user_id):
    """Find user by user id"""

    return User.query.filter(User.id == user_id).first()


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


def find_itinerary_by_user(user):
    """Find and return itinerary per user"""

    return Itinerary.query.filter(Itinerary.user == user).all()


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


def find_entries_by_itinerary(itinerary):
    """Find and return all entries for an itinerary"""

    return Entry.query.filter(Entry.itinerary == itinerary).all()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)