import sqlalchemy as sa
import datetime
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase


class Location(SqlAlchemyBase):
    __tablename__: "locations"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    org = sa.Column(sa.String, index=True)
    street = sa.Column(sa.String)
    city = sa.Column(sa.String, index=True)
    state = sa.Column(sa.String)
    country = sa.Column(sa.String, index=True)

    height_in = sa.Column(sa.Integer)
    height_cm = sa.Column(sa.Integer)
    standing_capacity = sa.Column(sa.Integer)
    adjustable = sa.Column(sa.Boolean)
    seating = sa.Column(sa.Boolean)
    power = sa.Column(sa.Boolean)
    foodbev = sa.Column(sa.Boolean)
    comments = sa.column(sa.String)

    reviews = orm.relation('Review', back_populates='location')