from data import db_session

from data.games import Games

"""Добавление игры в таблицу"""

game = Games()
game.image = input('Название файла')
game.answer_choice = input('Варианты ответа через "**"')
game.answer = input('Правильный ответ')
question = input('Вопрос (если оставить пустым, будет вопрос по умолчанию)')
if not question == '':
    game.question = question

db_session.global_init("db/mailing.sqlite")
session = db_session.create_session()
session.add(game)
session.commit()
