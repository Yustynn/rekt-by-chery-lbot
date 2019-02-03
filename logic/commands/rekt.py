from ..db.db import record_rekt
from ..misc.config import PEOPLE
from ..misc.helpers import get_target_person

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# def rekt(bot, update):
#     target_person = get_target_person(update)

#     if target_person:
#         record_rekt(target_person)
#         response = f'{target_person} got rekt'

#     else:
#         response = 'who?'

#     bot.send_message(
#         chat_id=update.message.chat_id,
#         text=response
#     )


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

# updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
