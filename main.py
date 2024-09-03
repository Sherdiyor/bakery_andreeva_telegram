import os
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from api_request import get_forms, delete_form
from dotenv import load_dotenv

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID'))

bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN)


def orders(page, forms):
    for form in forms:
        for key, value in form.items():
            if key == 'id' and value == page:
                message = f'Новый заказ от клиента: {form["name"]}\n\nТелефон клиента: {form["phone"]}\nОписание заказа: {form["comment"]}'
                return message
            continue


def wake_up(update, context):
    logging.info('Запрос на старт!')
    chat = update.effective_chat
    if chat.id == ADMIN_CHAT_ID:
        orders_cnt = len(get_forms())
        keyboard = [[InlineKeyboardButton(
            'К заказам', callback_data='to_orders')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = (
            'Привет!\n'
            f'Количество невыполненных заказов: {orders_cnt}'
        )
        context.bot.send_message(
            chat_id=chat.id,
            text=message,
            reply_markup=reply_markup
        )
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text='Вы не админ!'
        )


def callback_handler(update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'to_orders':
        forms = get_forms()
        for i in forms:
            id = i.get('id')
            keyboard = [[InlineKeyboardButton(
                'Выполнен', callback_data=f'complete_{id}')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(
                chat_id=query.message.chat_id,
                text=orders(id, forms),
                reply_markup=reply_markup
            )
    elif 'complete' in query.data:
        id = query.data.split('_')[1]
        delete_form(id)
        query.edit_message_text(text='Данный заказ выполнен!')


def main():
    logging.info('Бот запустился!')
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
