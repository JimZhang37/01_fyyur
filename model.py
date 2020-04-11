from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.types import PickleType
import datetime

db = SQLAlchemy()
migrate = Migrate()

def db_setup(app):
    db.init_app(app)
    migrate.init_app(app,db)

    


class Show(db.Model):
    __talbename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    artist = db.relationship('Artist', backref='shows_of_artist')
    venue = db.relationship('Venue', backref='shows_at_venue')

    def __repr__(self):
        return f'the show {self.id} has artist {self.artist_id} at venue{self.venue_id} in {self.start_time}'

    def short(self):
        return {
        "venue_id": self.venue_id,
        "venue_name": self.venue_for_show.name,
        "venue_image_link": self.venue_for_show.image_link,
        "start_time": str(self.start_time)
        }

    def long(self):
        return {"venue_id": self.venue_id,
              "venue_name": self.venue_for_show.name,
              "artist_id": self.artist_id,
              "artist_name": self.artist_for_show.name,
              "artist_image_link":  self.artist_for_show.image_link,
              "start_time": str(self.start_time)
              }

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(PickleType)
    
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String)
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.String)
    seeking_description = db.Column(db.String)
    image_link = db.Column(db.String(500))

    show = db.relationship('Show', backref='venue_for_show')

    # past_shows, upcoming_shows, past_shows_count, upcoming_shows_count
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'num_upcoming_shows': self.num_upcoming_shows()
        }

    def long(self):
        return {
        "id": self.id,
        "name": self.name,
        "genres": self.genres,
        "city": self.city,
        "state": self.state,
        "phone": self.phone,
        "website": "https://www.gunsnpetalsband.com",
        "facebook_link": self.facebook_link,
        "seeking_venue": True,
        "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
        "image_link": self.image_link

    }

    def get_venue(self):
        return {
            'id': self.id,
            'name': self.name,
            'num_upcoming_shows': len(self.show)
        }

    def num_upcoming_shows(self):
        shows = self.shows_at_venue
        comingshowslist = list(filter(lambda x: x.start_time > datetime.datetime.now(), shows))
        return len(comingshowslist)

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(PickleType)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String)
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean())
    seeking_description = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    show = db.relationship('Show', backref='artist_for_show')
    # past_shows, upcoming_shows, past_shows_count, upcoming_shows_count
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def short(self):

        return {
            'id': self.id,
            'name': self.name,
            'num_upcoming_shows': self.num_upcoming_shows()
        }
    def long(self):

        return {
        "id": self.id,
        "name": self.name,
        "genres": self.genres,
        "city": self.city,
        "state": self.state,
        "phone": self.phone,
        "website": self.website,
        "facebook_link": self.facebook_link,
        "seeking_venue": True,
        "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
        "image_link": self.image_link

    }

    def num_upcoming_shows(self):
        '''
        provide input to short()
        '''
        shows = self.shows_of_artist
        comingshowslist = list(filter(lambda x: x.start_time > datetime.datetime.now(), shows))
        return len(comingshowslist)
        

