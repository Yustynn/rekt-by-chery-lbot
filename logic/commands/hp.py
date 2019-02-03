from datetime import datetime

from telegram import ParseMode

from ..misc.config import INIT_HP, PEOPLE
from ..misc.get_hps import get_hps


def hp(bot, update):
    hps = get_hps()

    text = '*Hitpoints Remaining*\n```'
    for person in PEOPLE:
        if hps[person] > 0:
            text += f'\n{person:10}: {hps[person]}/{INIT_HP}'
        else:
            text += f'\n{person:10}: DEAD'
    text += '```'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN
    )
