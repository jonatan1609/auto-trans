from .database import User
from pony.orm import db_session


@db_session
def exist_in_db(user):
    user = User.get(id=user)
    return bool(user)


@db_session
def get_native_language(user):
    user = User.get(id=user)
    if not bool(user):
        return False
    else:
        return user.native_language


@db_session
def add_to_db(user):
    User(id=user)


@db_session
def change_language(user_id, lang):
    user = User.get(id=user_id)
    if not bool(user):
        return False
    user.native_language = lang
