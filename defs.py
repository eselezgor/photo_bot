import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from data.mailing import Mailing
from data.tests import Tests
from data.facts import Facts
from data.games import Games
from data import db_session
import datetime
import random


def get_photo(owner, album):
    """Список id всех фото из альбома"""

    login, password = '79037726038', 'password'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)

    vk = vk_session.get_api()
    photo = vk.photos.get(owner_id=-owner, album_id=album)
    all_id = []
    for item in photo['items']:
        all_id += [f"photo{item['owner_id']}_{item['id']}"]
    return all_id


def add_mailing(id, how_often):
    """Добавление пользователя в список рассылок"""

    mail = Mailing()
    mail.id = id
    mail.how_often = how_often
    mail.next_send = datetime.datetime.now() + datetime.timedelta(days=(7 / how_often))
    session = db_session.create_session()
    session.add(mail)
    session.commit()


def add_facts(id, how_often):
    """Добавление пользователя в список рассылок фактов"""

    fact = Facts()
    fact.id = id
    fact.how_often = how_often
    fact.next_send = datetime.datetime.now() + datetime.timedelta(days=(7 / how_often))
    session = db_session.create_session()
    session.add(fact)
    session.commit()


def del_mailing(id):
    session = db_session.create_session()
    session.query(Mailing).filter(Mailing.id == id).delete()
    session.commit()


def del_fact(id):
    session = db_session.create_session()
    session.query(Facts).filter(Facts.id == id).delete()
    session.commit()


def del_test(id):
    session = db_session.create_session()
    session.query(Tests).filter(Tests.id == id).delete()
    session.commit()


def mailing_check():
    """Проверка рассылки"""

    session = db_session.create_session()
    for mail in session.query(Mailing).all():
        if mail.next_send <= datetime.datetime.now():
            mail.next_send = datetime.datetime.now() + datetime.timedelta(days=(7 / mail.how_often))
            session.commit()
            return mail.id
    return ''


def facts_check():
    try:
        session = db_session.create_session()
        for fact in session.query(Facts).all():
            if fact.next_send <= datetime.datetime.now():
                fact.next_send = datetime.datetime.now() + datetime.timedelta(days=(7 / fact.how_often))
                return fact.id
        return ''
    except Exception as e:
        print(e)
        return ''


def get_random_test():
    """Получение случайного теста"""

    session = db_session.create_session()
    test = random.choice(session.query(Tests).all())
    return [test.question, test.answer_choice, test.answer]


def get_random_game():
    """Случайная мини-игра"""

    session = db_session.create_session()
    games = random.choice(session.query(Games).all())
    return [games.image, games.question, games.answer_choice, games.answer]


def add_button(keyboard, text, new_line=True):
    """Добавение кнопки в клавиатуру"""

    keyboard = keyboard
    if new_line:
        keyboard.add_line()
    keyboard.add_button(text, color=VkKeyboardColor.DEFAULT)
    return keyboard
