from random import choice

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from ..db.db import record_rekt
from ..misc.config import PEOPLE, REKT_MESSAGES
from ..misc.helpers import get_target_person

def people_menu():
    keyboard = [
        [InlineKeyboardButton(person, callback_data=f'rekt/{person}')] for person in PEOPLE
    ]

    return InlineKeyboardMarkup(keyboard)

def rekt_scale_menu():
    keyboard = [
        [i] for i in range(1, 4)
    ]

    return InlineKeyboardMarkup(keyboard)


def rekt(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        reply_markup=people_menu(),
        text="Who got rekt?"
    )

    print('\n\n\n', update.message.chat_id, '\n\n\n')

def handle_rekt(bot, update):
    print(f'handling rekt, {update.callback_query.data}')
    who = update.callback_query.data.replace('rekt/', '')
    print(who)
    record_rekt(who, 1)
    print()

    print(bot.send_message)
    bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text=choice(REKT_MESSAGES).replace('$NAME', who)
    )

rekt_callbacks = [
    (handle_rekt, r'rekt/.+')
]
