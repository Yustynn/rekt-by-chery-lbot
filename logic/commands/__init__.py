from telegram.ext import CallbackQueryHandler, CommandHandler
from .cleardb import cleardb
from .graph import graph, graph_callbacks
from .hp import hp
from .rekt import rekt, rekt_callbacks
from .seeddb import seeddb
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
register_command('cleardb_yp', cleardb)
register_command('hp', hp)
register_command('graph', graph)
register_command('rekt', rekt)
register_command('seeddb_yp', seeddb)

register_callbacks(rekt_callbacks)
register_callbacks(graph_callbacks)
