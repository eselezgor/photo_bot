import sqlalchemy
from .db_session import SqlAlchemyBase


class Games(SqlAlchemyBase):
    """Таблица с играми"""

    __tablename__ = 'games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    image = sqlalchemy.Column(sqlalchemy.String)  # Название картинки в папке static/games
    question = sqlalchemy.Column(sqlalchemy.String, default='Что спряталось на этой картинке?')
    answer_choice = sqlalchemy.Column(sqlalchemy.String)  # Четыре варианта ответа через **
    answer = sqlalchemy.Column(sqlalchemy.String)
