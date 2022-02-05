# (c) @SpEcHIDe

from sqlalchemy import (
    Column,
    String
)
from userbot.modules.sql_helper import (
    SESSION,
    BASE
)


class blacklistbot(BASE):
    __tablename__ = "blacklistbot"
    chat_id = Column(String(14), primary_key=True)
    # reason = Column(UnicodeText)

    def __init__(self, chat_id):
        self.chat_id = int(chat_id)
        # self.reason = reason

    def __repr__(self):
        return "<BL %s>" % self.chat_id


blacklistbot.__table__.create(checkfirst=True)


def add_user_to_bl(chat_id: int):
    """Adding the user to the blacklist"""
    __user = blacklistbot(str(chat_id))
    SESSION.add(__user)
    SESSION.commit()


def check_is_black_list(chat_id):
    """check if blacklisted"""
    try:
        return SESSION.query(blacklistbot).filter(
            blacklistbot.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def rem_user_from_bl(chat_id):
    """remove from bl"""
    __user = SESSION.query(blacklistbot).get(str(chat_id))
    if __user:
        SESSION.delete(__user)
        SESSION.commit()


def all_bl_users():
    """get all bl users"""
    __user = SESSION.query(blacklistbot).all()
    SESSION.close()
    return __user
