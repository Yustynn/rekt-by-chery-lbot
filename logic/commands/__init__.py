from telegram.ext import CommandHandler
from .graph import graph
from .rekt import rekt
from .start import start

def register_all_commands(dispatcher):
    def register(name, f):
        dispatcher.add_handler(
            CommandHandler(name, f)
        )

    register('start', start)
    register('graph', graph)
    register('rekt', rekt)
