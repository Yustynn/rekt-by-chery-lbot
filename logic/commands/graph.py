import matplotlib.pyplot as plt

from ..db.db import get_rekt_records
from ..misc.helpers import get_target_person

GRAPH_PHOTO_PATH = './graph.png'

def graph(bot, update):
    target_person = get_target_person(update)

    records = get_rekt_records(target_person)
    xs = list(records.keys())
    ys = [len(ls) for ls in records.values()]

    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    ax.set_title(f"{target_person}'s Weekly Wreckage")
    fig.savefig(GRAPH_PHOTO_PATH)

    photo = open(GRAPH_PHOTO_PATH, 'rb')

    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=photo
    )

    photo.close()
    os.remove(GRAPH_PHOTO_PATH)
