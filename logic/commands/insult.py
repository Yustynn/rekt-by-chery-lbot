from ..misc.insults import generate_anonymous_insult


def insult(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=generate_anonymous_insult()
    )
