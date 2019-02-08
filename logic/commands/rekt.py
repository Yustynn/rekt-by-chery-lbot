from random import choice, random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from ..db.db import record_rekt
from ..misc.config import CRITICAL_HIT_CHANCE, CRITICAL_HIT_MULTIPLIER, DEAD_MESSAGES, \
    DAMAGE_MULTIPLIER, DEAD_REKT_MESSAGES, INIT_HP, REKT_MESSAGES, SEVERITY_RANKINGS
from ..misc.helpers import build_people_menu, get_target_person
from ..misc.get_hps import get_hps

state = {
    'message_id': None,
    'chat_id': None,
    'who': None,
    'by': None,
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
        reply_markup=build_people_menu('rekt_by'),
        text="Who was the wrecker?"
    )

    state['message_id'] = message.message_id
    state['chat_id'] = message.chat_id

def handle_rekt_by(bot, update):
    by = update.callback_query.data.replace('rekt_by/', '')
    state['by'] = by

    bot.edit_message_text(
        chat_id=state['chat_id'],
        message_id=state['message_id'],
        text=f"Who did {by} wreck?"
    )

    bot.edit_message_reply_markup(
        chat_id=state['chat_id'],
        message_id=state['message_id'],
        reply_markup=build_people_menu('rekt_who'),
    )


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
    by = state['by']
    severity = int(severity)

    is_critical = random() < CRITICAL_HIT_CHANCE

    if is_critical:
        severity *= CRITICAL_HIT_MULTIPLIER

    old_hp = get_hps()[who]
    record_rekt(who, by, severity)
    new_hp = old_hp - severity * DAMAGE_MULTIPLIER

    is_dead = new_hp <= 0
    is_newly_dead = old_hp > 0 and is_dead
    print(old_hp, new_hp, is_newly_dead, '\n\n')

    text = choice(REKT_MESSAGES).replace('$NAME', who)
    if is_critical:
        text += f'\n\nCritical Hit! Damage multiplied by {CRITICAL_HIT_MULTIPLIER}'

    text += f'\n\n{who} has {new_hp}/{INIT_HP} HP left.'

    if is_newly_dead:
        text += '\n\n' + choice(DEAD_MESSAGES).replace('$NAME', who)
    elif is_dead:
        text += f' {who} was already dead.'
        text += '\n\n' + choice(DEAD_REKT_MESSAGES).replace('$NAME', who)

    bot.edit_message_text(
        chat_id=state['chat_id'],
        message_id=state['message_id'],
        text=text
    )

rekt_callbacks = [
    (handle_rekt_by, r'rekt_by/.+'),
    (handle_rekt_who, r'rekt_who/.+'),
    (handle_rekt_final, r'rekt_final/.+')
]
