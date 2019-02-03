from telegram.ext import Updater
from .misc.config import TOKEN

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
