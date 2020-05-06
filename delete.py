from data import db_session
from data.tests import Tests
from data.games import Games

db_session.global_init('db/mailing.sqlite')
session = db_session.create_session()
session.query(Games).filter(Games.id == int(input('id'))).delete()
session.commit()
