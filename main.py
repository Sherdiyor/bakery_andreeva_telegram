from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = '7476144216:AAEvl2_NHLcQp3CYt4S093FhK0Wr24KjVco'

bot = Bot(TOKEN)
update = Updater(TOKEN)


def wake_up(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет!',
    )


def main():
    update.dispatcher.add_handler(CommandHandler('start', wake_up))
    update.start_polling()
    update.idle()


if __name__ == '__main__':
    main()
