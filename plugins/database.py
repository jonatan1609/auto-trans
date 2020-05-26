from pony.orm import PrimaryKey, Database, Optional
from os.path import exists


db = Database()


class User(db.Entity):
    id = PrimaryKey(int)
    native_language = Optional(str)


if exists('../db.sql'):
    db.bind(provider='sqlite', filename='../db.sql')
else:
    db.bind(provider='sqlite', filename='../db.sql', create_db=True)
db.generate_mapping(create_tables=True)
