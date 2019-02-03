from ..db.db import collection

def cleardb(bot, update):
    collection.delete_many({})

    bot.send_message(
        chat_id=update.message.chat_id,
        text="DB Cleared."
    )
