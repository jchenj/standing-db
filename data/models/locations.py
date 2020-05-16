import sqlalchemy as sa
import datetime
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase

#! TODO: fill in columns
class Location(SqlAlchemyBase):
    __tablename__: "locations"
    id = sa.Column()
    created_date = sa.Column()
    org = sa.Column()
    street = sa.Column()
    city = sa.Column()
    state = sa.Column()
    country = sa.Column()
    height = sa.Column()
    adjustsable = sa.Column()
    seating = sa.Column()
    power = sa.Column()
    foodbev = sa.Column()
    comments = sa.column()