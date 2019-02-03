from pytz import timezone
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .config import PEOPLE

def build_people_menu(callback_prepend):
    keyboard = [
        [InlineKeyboardButton(person, callback_data=f'{callback_prepend}/{person}')] for person in PEOPLE
    ]

    return InlineKeyboardMarkup(keyboard)

def get_target_person(update):
    text = ' '.join(
        update.message.text.split(' ')[1:]
    )

    who = text.strip()

    matches = [person for person in PEOPLE if person.startswith(who)]

    if not matches or who is '' or len(matches) > 1:
        return ''

    return matches[0]


def localize_datetime(dt):
    return timezone('Asia/Singapore').localize(dt)

def to_datestring(dt):
    return dt.strftime('%d/%m/%Y')
