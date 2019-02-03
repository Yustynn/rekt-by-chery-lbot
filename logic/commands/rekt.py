from random import choice

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from ..db.db import record_rekt
from ..misc.config import INIT_HP, DEAD_MESSAGES, REKT_MESSAGES, SEVERITY_RANKINGS
from ..misc.helpers import build_people_menu, get_target_person
from ..misc.get_hps import get_hps

state = {
    'message_id': None,
    'chat_id': None
}

def build_severity_menu(person):
    rankings = choice(SEVERITY_RANKINGS)
    keyboard = [
        [InlineKeyboardButton(text, callback_data=f'rekt_final/{person}/{i+1}')] for i, text in enumerate(rankings)
    ]

    return InlineKeyboardMarkup(keyboard)


def rekt(bot, update):
    message = bot.send_message(
        chat_id=update.message.chat_id,
        reply_markup=build_people_menu('rekt_who'),
        text="Who got rekt?"
    )

    state['message_id'] = message.message_id
    state['chat_id'] = message.chat_id

def handle_rekt_who(bot, update):
    who = update.callback_query.data.replace('rekt_who/', '')

    bot.edit_message_text(
        chat_id=state['chat_id'],
        message_id=state['message_id'],
        text=f"How burnt did {who} get?"
    )

    bot.edit_message_reply_markup(
        chat_id=state['chat_id'],
        message_id=state['message_id'],
        reply_markup=build_severity_menu(who),
        text="How burnt?"
    )

def handle_rekt_final(bot, update):
    who, severity = update.callback_query.data.split('/')[1:]
    severity = int(severity)

    record_rekt(who, severity)
    hp = get_hps()[who]

    text = choice(REKT_MESSAGES).replace('$NAME', who)
    if hp > 0:
        text += f'\n{who} has {hp}/{INIT_HP} HP left.'
    else:
        text += '\n\n' + choice(DEAD_MESSAGES).replace('$NAME', who)

    bot.edit_message_text(
        chat_id=state['chat_id'],
        message_id=state['message_id'],
        text=text
    )

rekt_callbacks = [
    (handle_rekt_who, r'rekt_who/.+'),
    (handle_rekt_final, r'rekt_final/.+')
]
