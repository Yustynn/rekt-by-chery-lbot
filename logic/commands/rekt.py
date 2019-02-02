from ..db.db import record_rekt
from ..misc.helpers import get_target_person

def rekt(bot, update):
    target_person = get_target_person(update)

    if target_person:
        record_rekt(target_person)
        response = f'{target_person} got rekt'

    else:
        response = 'Who?'

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response
    )
