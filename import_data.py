import datetime
import random

from data import session_factory
from data.models.locations import Location
from data.models.reviews import Review

from services import data_service


def import_if_empty():
    __import_locations()
    __import_reviews()


def __import_locations():
    session = session_factory.create_session()
    if session.query(Location).count() > 1:
        return

    location = Location()
    location.org = 'Org2'
    location.space = 'cafe'
    location.city = 'Seattle'
    location.country = 'USA'
    location.height_in = random.randint(35, 50)
    session.add(location)

    location = Location()
    location.org = 'Org2'
    location.space = 'cafe'
    location.city = 'Seattle'
    location.country = 'USA'
    location.height_in = random.randint(35, 50)
    session.add(location)

    location = Location()
    location.org = 'Org3'
    location.space = 'atrium'
    location.city = 'Vancouver'
    location.country = 'Canada'
    location.height_in = random.randint(35, 50)
    session.add(location)

    location = Location()
    location.org = 'Org4'
    location.space = 'lobby'
    location.city = 'Singapore'
    location.country = 'Singapore'
    location.height_in = random.randint(35, 50)
    session.add(location)

    session.commit()


def __import_reviews():
    session = session_factory.create_session()
    if session.query(Review).count() > 0:
        return

    #! TODO: add two reviews per location
    session.add(review)
    session.commit()
