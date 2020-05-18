import sqlalchemy as sa
import datetime
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase


class Review(SqlAlchemyBase):
    __tablename__ = "reviews"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    reviewer = sa.Column(sa.String, index=True)
    comments = sa.Column(sa.String)

    location_id = sa.Column(sa.Integer, sa.ForeignKey('locations.id'), nullable=False)
    location = orm.relation('Location', back_populates='review')
