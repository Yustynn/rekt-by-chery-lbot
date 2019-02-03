from random import choice

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from ..db.db import record_rekt
from ..misc.config import REKT_MESSAGES, SEVERITY_RANKINGS
from ..misc.helpers import build_people_menu, get_target_person

def build_severity_menu(person):
    rankings = choice(SEVERITY_RANKINGS)
    keyboard = [
        [InlineKeyboardButton(text, callback_data=f'rekt_final/{person}/{i+1}')] for i, text in enumerate(rankings)
    ]

    return InlineKeyboardMarkup(keyboard)


def rekt(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        reply_markup=build_people_menu('rekt_who'),
        text="Who got rekt?"
    )

def handle_rekt_who(bot, update):
    who = update.callback_query.data.replace('rekt_who/', '')

    bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        reply_markup=build_severity_menu(who),
        text="How burnt?"
    )


    print(bot.send_message)

def handle_rekt_final(bot, update):
    who, severity = update.callback_query.data.split('/')[1:]
    severity = int(severity)

    record_rekt(who, severity)

    bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text=choice(REKT_MESSAGES).replace('$NAME', who)
    )

rekt_callbacks = [
    (handle_rekt_who, r'rekt_who/.+'),
    (handle_rekt_final, r'rekt_final/.+')
]
