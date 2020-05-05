import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Mailing(SqlAlchemyBase):
    """Подписаться на рассылку"""

    __tablename__ = 'mailing'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    last_send = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    how_often = sqlalchemy.Column(sqlalchemy.Integer, default=2)  # Times in a week
    next_send = sqlalchemy.Column(sqlalchemy.DateTime)
