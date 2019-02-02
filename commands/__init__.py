from telegram.ext import CommandHandler
from commands.graph import graph
from commands.rekt import rekt
from commands.start import start

def register_all_commands(dispatcher):
    def register(name, f):
        dispatcher.add_handler(
            CommandHandler(name, f)
        )

    register('start', start)
    register('graph', graph)
    register('rekt', rekt)
