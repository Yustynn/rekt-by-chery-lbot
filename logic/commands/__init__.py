from telegram.ext import CommandHandler
from .graph import graph
from .rekt import rekt
from .start import start
from ..updater import dispatcher

def register_command(name, f):
    dispatcher.add_handler(
        CommandHandler(name, f)
    )

register_command('start', start)
register_command('graph', graph)
register_command('rekt', rekt)
