import datetime
import sys

import import_data
from data import session_factory
from infrastructure.numbers import try_int
from infrastructure.switchlang import switch
from data.models.locations import Location
from services import data_service


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
    import_data.import_if_empty()


def browse_locations():
    print("********* Browse all locations ********* ")
    all_locations = data_service.get_all_locations()

    for idx, l in enumerate(all_locations, start=1):
        print(f"{idx}. {l.org} {l.space} - {l.city} {l.country}, "
              f"{l.standing_capacity} standing spaces. Height: {l.height_in}in")
    print()
    return all_locations


def find_locations():
    print("********* All cities in database ********* ")
    all_cities = data_service.get_all_cities()

    for idx, c in enumerate(all_cities, start=1):
        print(f"{idx}. {c}")
    chose_it = try_int(input("Choose city by typing its number: ")) -1

    if not (0 <= chose_it < len(all_cities)):
        print("Error. Pick another number")
        return

    city = all_cities[chose_it]
    all_city_locations = data_service.get_locations_by_city(city)

    loc_term = 'location'
    if len(all_city_locations) != 1:
        loc_term += 's'

    print()
    print(f"{len(all_city_locations)} {loc_term} in this city")
    print()
    for c in all_city_locations:
        print(f"* {c.org} {c.space} - {c.city} {c.country}, "
              f"{c.standing_capacity} standing spaces. Height: {c.height_in}in")
    print()
    return all_city_locations


def read_reviews():
    print("********* All reviews ********* ")
    all_reviews = data_service.get_all_reviews()
    for r in all_reviews:
        print(f"{r.created_date.date()} {r.location.org} {r.location.space}: {r.text}. {r.reviewer}")
    print()


def exit_app():
    print("")
    print("Goodbye!")
    sys.exit(0)


if __name__ == '__main__':
    main()










