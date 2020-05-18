import datetime
import random
from typing import List

from data import session_factory
from data.models.locations import Location
from data.models.reviews import Review


def get_default_location():
    session = session_factory.create_session()

    location = session.query(Location).filter(Location.org == 'Test org 1').first()
    if location:
        return location

    location = Location()
    location.org = 'Test org 1'
    location.space = 'Ground floor cafe'
    location.city = 'Vancouver'
    location.country = 'Canada'
    location.height_in = 48
    location.standing_capacity = 20
    location.adjustable = False
    location.seating = True
    location.power = True
    location.foodbev = True
    location.wifi = True

    session.add(location)
    session.commit()

    return location


def get_all_locations() -> List[Location]:
    session = session_factory.create_session()
    locations = session.query(Location)

    return list(locations)


def get_all_cities():
    session = session_factory.create_session()
    cities = session.query(Location.city).distinct()

    return list(cities)


def get_all_reviews() -> List[Review]:
    session = session_factory.create_session()
    reviews = session.query(Review)

    return list(reviews)

