import os
from random import choice

import matplotlib.pyplot as plt

from ..db.db import get_rekt_records
from ..misc.helpers import build_people_menu
from ..misc.config import DAMAGE_MULTIPLIER

GRAPH_PHOTO_PATH = './graph.png'
GRAPH_LINE_COLORS = [
    'b',
    'g',
    'r',
    'c',
    'm',
    'y',
    'k'
]

def graph(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        reply_markup=build_people_menu('graph_who'),
        text="Graph whose wreckage?"
    )

def handle_graph_who(bot, update):
    who = update.callback_query.data.replace('graph_who/', '')

    records = get_rekt_records(who, fields=['severity'])
    xs = list(records.keys())
    ys = [sum([r['severity'] * DAMAGE_MULTIPLIER for r in rekts]) for rekts in records.values()]

    fig, ax = plt.subplots()

    ax.plot(xs, ys, color=choice(GRAPH_LINE_COLORS), lw=3)

    ax.set_title(f"{who}'s 5-Day Damage")
    ax.set_xlabel("Date")
    ax.set_ylabel("Daily Damage")

    fig.savefig(GRAPH_PHOTO_PATH)
    photo = open(GRAPH_PHOTO_PATH, 'rb')

    bot.send_photo(
        chat_id=update.callback_query.message.chat_id,
        photo=photo
    )

    photo.close()
    os.remove(GRAPH_PHOTO_PATH)

graph_callbacks = [
    (handle_graph_who, r'graph_who/.+')
]
