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
    if session.query(Location).count() > 0:
        return

    location = Location()
    location.org = 'Org1'
    location.space = 'ground floor cafe'
    location.city = 'Vancouver'
    location.country = 'Canada'
    location.standing_capacity = 5
    location.height_in = random.randint(35, 50)
    session.add(location)

    location = Location()
    location.org = 'Org2'
    location.space = 'cafe'
    location.city = 'Seattle'
    location.country = 'USA'
    location.standing_capacity = 10
    location.height_in = random.randint(35, 50)
    session.add(location)

    location = Location()
    location.org = 'Org3'
    location.space = 'atrium'
    location.city = 'Vancouver'
    location.country = 'Canada'
    location.standing_capacity = 15
    location.height_in = random.randint(35, 50)
    session.add(location)

    location = Location()
    location.org = 'Org4'
    location.space = 'lobby'
    location.city = 'Singapore'
    location.country = 'Singapore'
    location.standing_capacity = 3
    location.height_in = random.randint(35, 50)
    session.add(location)

    session.commit()


def __import_reviews():
    session = session_factory.create_session()
    if session.query(Review).count() > 0:
        return

    reviewers = [
        'Reviewer 1',
        'Reviewer 2',
        'Reviewer 3'
    ]

    locations = list(session.query(Location).all())

    sample_text = [
        'Positive review',
        'Neutral review',
        'Negative review'
    ]

    # create 10 reviews
    COUNT = 10
    for n in range(0, COUNT):
        review = Review()
        review.reviewer = random.choice(reviewers)
        review.location = random.choice(locations)
        review.text = random.choice(sample_text)
        session.add(review)

    session.commit()
