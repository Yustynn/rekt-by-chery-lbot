from telegram.ext import CallbackQueryHandler, CommandHandler
from .graph import graph
from .rekt import rekt, rekt_callbacks
from .start import start
from ..updater import dispatcher

def register_callbacks(callbacks):
    for callback, pattern in callbacks:
        dispatcher.add_handler(
            CallbackQueryHandler(callback, pattern=pattern)
        )

def register_command(name, f):
    dispatcher.add_handler(
        CommandHandler(name, f)
    )


register_command('start', start)
register_command('graph', graph)
register_command('rekt', rekt)

register_callbacks(rekt_callbacks)
