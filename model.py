"""Travel App Itininary Database"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """Data model for a user"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(30))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User id={self.id}, username={self.username}, email={self.email}>'


class Itinerary(db.Model):
    """Data model for an itinerary"""

    __tablename__ = 'itineraries'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Itinerary id={self.id}, name={self.name}, start_date={self.start_date}'


class Entry(db.Model):
    """Data model for an entry"""

    __tablename__ = 'entries'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String)
    image = db.Column(db.String)
    comment = db.Column(db.Text)
    location = db.Column(db.String(50))

    trip_day = db.Column(db.DateTime)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Entry id={self.id}, name={self.name}, location={self.location}'


class PlaceType(db.Model):
    """Data model for a place type"""

    __tablename__ = 'place_types'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    place_type = db.Column(db.String(15))

    def __repr__(self):
        return f'<PlaceType id={self.id}, place_type={self.place_type}'


class EntryType(db.Model):
    """Data model for an entry type"""

    __tablename__ = 'entry_types'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    place_type_id = db.Column(db.Integer, db.ForeignKey('place_types.id'))
    entry_id = db.Column(db.Integer, db.ForeignKey('entries.id'))

    def __repr__(self):
        return f'<EntryType id={self.id}, place_type_id={self.place_type_id}'

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print('Connected to db!')
