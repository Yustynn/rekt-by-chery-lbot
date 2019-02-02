import os

from telegram.ext import Updater

from logic.misc.config import TOKEN
from logic.commands import register_all_commands

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

register_all_commands(dispatcher)
updater.start_polling()
