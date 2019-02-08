from datetime import datetime

from ..db.db import get_rekt_records
from .config import DAMAGE_MULTIPLIER, INIT_HP, PEOPLE
from .helpers import to_datestring

def get_hps():
    hps = {person: INIT_HP for person in PEOPLE}
    records = get_rekt_records(num_days=1)

    today = to_datestring(datetime.now())
    for record in records[today]:
        print(record)
        hps[record['who']] -= record['severity'] * DAMAGE_MULTIPLIER
        hps[record['by']] += record['severity'] * DAMAGE_MULTIPLIER

    return hps
