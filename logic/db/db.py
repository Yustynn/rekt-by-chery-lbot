from collections import OrderedDict
from datetime import datetime, timedelta

from pymongo import MongoClient
from bson.codec_options import CodecOptions
import pytz

from ..misc.helpers import localize_datetime, to_datestring
from ..misc.secrets import DB_USER, DB_PASSWORD

db = MongoClient(host='ds060649.mlab.com', port=60649)['cherylbot']
db.authenticate(DB_USER, DB_PASSWORD)

collection = db['wreckage'].with_options(
    codec_options = CodecOptions(
        tz_aware = True,
        tzinfo = pytz.timezone('Asia/Singapore')
    )
)

def record_rekt(who, severity):
    collection.insert_one({
        'who': who,
        'severity': severity,
        'timestamp': localize_datetime(datetime.now())
    })

    print(f'Recorded {who} at {datetime.now()}')
    print(collection.find()[0])

def get_rekt_records(who=None, num_days=5):
    start = localize_datetime(datetime.now().replace(hour=0, minute=0)) - timedelta(days=num_days-1)

    query = {'timestamp': {'$gt': start}}

    if who:
        query['who'] = who

    docs = collection.find(query)
    rekts_by_date = {to_datestring(start + timedelta(days=i)): [] for i in range(num_days)}

    for doc in docs:
        date = to_datestring(doc['timestamp'])
        rekts_by_date[date].append(doc['severity'])

    return rekts_by_date
