from telegram.ext import Updater
from .misc.secrets import TOKEN

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
