import datetime
import random
from typing import List

from data import session_factory
from data.models.locations import Location
from data.models.reviews import Review


def get_all_locations() -> List[Location]:
    session = session_factory.create_session()
    locations = session.query(Location).all()

    return list(locations)


def get_all_cities():
    session = session_factory.create_session()
    cities = session.query(Location.city).distinct()

    return [i[0] for i in cities]


def get_locations_by_city(city):
    session = session_factory.create_session()
    locations = session.query(Location).filter(Location.city == city).all()

    return list(locations)


def get_all_reviews() -> List[Review]:
    session = session_factory.create_session()
    reviews = session.query(Review).all()

    return list(reviews)

