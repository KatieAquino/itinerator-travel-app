"""Travel App Itininary Database"""

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date

db = SQLAlchemy()


class User(db.Model):
    """Data model for a user"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(30))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(128))

    # hash password for database security
    def set_password(self, password):
        """Hash password for security"""

        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Checks if password matches"""

        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User id={self.id}, username={self.username}, email={self.email}>'


class Itinerary(db.Model):
    """Data model for an itinerary"""

    __tablename__ = 'itineraries'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))

    user = db.relationship('User', backref='users')
    entry = db.relationship('Entry', backref='entries')

    def __repr__(self):
        return f'<Itinerary id={self.id}, name={self.name}, start_date={self.start_date}'


class Entry(db.Model):
    """Data model for an entry"""

    __tablename__ = 'entries'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    url = db.Column(db.String)
    image = db.Column(db.String)
    comment = db.Column(db.Text)
    location = db.Column(db.String(50))

    trip_day = db.Column(db.Integer)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'))
    complete = db.Column(db.Boolean)

    itinerary = db.relationship('Itinerary', backref='itineraries')
    types = db.relationship('PlaceType',
                            secondary='entry_types',
                            backref='place_types')

    def __repr__(self):
        return f'<Entry id={self.id}, name={self.name}, location={self.location}'


class Location(db.Model):
    """Locations that have been searched."""

    __tablename__ = 'locations'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location = db.Column(db.String(50))

    def __repr__(self):
        return f'<Location id={self.id}, location={self.location}>'


class Place(db.Model):
    """Place information for user."""

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    wikipedia = db.Column(db.Text)
    xid = db.Column(db.String(50))
    name = db.Column(db.Text)
    image = db.Column(db.Text)
    extract = db.Column(db.Text)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    location = db.relationship('Location', backref='locations')

    def __repr__(self):
        return f'<Place id={self.id}, name={self.name}>'

class PlaceType(db.Model):
    """Data model for a place type"""

    __tablename__ = 'place_types'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    place_type = db.Column(db.String(15))

    def __repr__(self):
        return f'<PlaceType id={self.id}, place_type={self.place_type}>'


class EntryType(db.Model):
    """Data model for an entry type"""

    __tablename__ = 'entry_types'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    place_type_id = db.Column(db.Integer, db.ForeignKey('place_types.id'))
    entry_id = db.Column(db.Integer, db.ForeignKey('entries.id'))

    def __repr__(self):
        return f'<EntryType id={self.id}, place_type_id={self.place_type_id}'


def connect_to_db(flask_app, db_uri='postgresql:///testdb', echo=True):
    """Connect to database"""

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print('Connected to db!')
