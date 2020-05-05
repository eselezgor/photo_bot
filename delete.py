from data import db_session
from data.tests import Tests

db_session.global_init('db/mailing.sqlite')
session = db_session.create_session()
session.query(Tests).filter(Tests.id == int(input('id'))).delete()
session.commit()
