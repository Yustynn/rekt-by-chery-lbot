from datetime import datetime, timedelta
from random import randint

from ..db.db import collection
from ..misc.config import PEOPLE
from ..misc.helpers import localize_datetime

MAX_PER_DAY = 3
NUM_DAYS = 10

def seeddb(bot, update):
    now = datetime.now()

    to_insert = []
    for person in PEOPLE:
        for dt in [now - timedelta(days=i) for i in range(NUM_DAYS)]:
            for i in range(randint(0, MAX_PER_DAY)):
                to_insert.append({
                    'timestamp': localize_datetime(dt),
                    'who': person,
                    'severity': randint(1, 3)
                })

    collection.insert_many(to_insert)

    bot.send_message(
        chat_id=update.message.chat_id,
        text="DB Seeded."
    )
