import sqlalchemy as sa
import datetime
from sqlalchemy import orm
from data.sqlalchemybase import SqlAlchemyBase

#! TODO: fill in columns
class Review(SqlAlchemyBase):
    class Review(SqlAlchemyBase):
        __tablename__: "reviews"
        id = sa.Column()
        created_date = sa.Column()
        reviewer = sa.Column()
        comments = sa.column()
        location_id = sa.Column(sa.Integer, sa.ForeignKey('locations.id'), nullable=False)
        location = orm.relation('Location', back_populates='review')
