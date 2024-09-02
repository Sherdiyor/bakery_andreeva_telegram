from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from api_request import get_forms, delete_form

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

BOT_TOKEN = '7476144216:AAEvl2_NHLcQp3CYt4S093FhK0Wr24KjVco'
ADMIN_CHAT_ID = 564717931

bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN)


def orders(page):
    forms = get_forms()
    form = forms[page]
    message = f'Новый заказ от клиента: {form["name"]}\n\nТелефон клиента: {form["phone"]}\nОписание заказа: {form["comment"]}'
    return message


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
        for i in range(len(get_forms())):
            keyboard = [[InlineKeyboardButton(
                'Выполнен', callback_data=f'complete_{i}')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(
                chat_id=query.message.chat_id,
                text=orders(i),
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
