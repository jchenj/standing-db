import datetime
import sys

from data import session_factory
from infrastructure.numbers import try_int
from infrastructure.switchlang import switch
from data.models.locations import Location
from services import data_service

location: Location = None


def main():
    setup_db()

    options = "Enter a command: [b]rowse, [f]ind, [r]ead reviews, e[x]it:  "
    cmd = "NOT SET"

    while cmd:
        cmd = input(options).lower().strip()
        with switch(cmd) as s:
            s.case('b', browse_locations)
            s.case('f', find_locations)
            s.case('r', read_reviews)
            s.case(['x', ''], exit_app)
            s.default(lambda: print(f"Not a valid command: {cmd}"))


def setup_db():
    global location
    session_factory.global_init('standing_db.sqlite')
    session_factory.create_tables()
    location = data_service.get_default_location()
    print("Found default location: {}, {}".format(location.org, location.space))


def browse_locations():
    print("********* Browse all locations ********* ")
    all_locations = []
    #! TODO show all locations
    print()
    return all_locations


def find_locations():
    print("********* Choose a city ********* ")
    cities = []
    #! TODO: choose city
    city = None
    #! TODO: set chosen city
    locations = []
    print(f"********* {len(locations)} locations in {city} ********* ")
    #! TODO: show locations from chosen city


def read_reviews():
    print("********* Read reviews ********* ")


def exit_app():
    print("")
    print("Goodbye!")
    sys.exit(0)


if __name__ == '__main__':
    main()










