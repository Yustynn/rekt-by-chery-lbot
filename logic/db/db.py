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

def record_rekt(who):
    collection.insert_one({
        'who': who,
        'timestamp': localize_datetime(datetime.now())
    })

    print(f'Recorded {who} at {datetime.now()}')
    print(collection.find()[0])

def get_rekt_records(who=None, num_days=10):
    start = localize_datetime(datetime.now().replace(hour=0, minute=0)) - timedelta(days=num_days-1)

    #query = {'timestamp': {'gt': start}}
    query = {}

    if who:
        query['who'] = who

    print('Query', query)
    print('who', who)

    docs = collection.find({'who': who})
    docs_by_date = {to_datestring(start + timedelta(days=i)): [] for i in range(num_days)}
    print(docs_by_date)

    for doc in docs:
        date = to_datestring(doc['timestamp'])
        docs_by_date[date].append(doc['who'])

    print(f'Num docs: {len(list(docs))}')
    print(docs_by_date)

    return docs_by_date

