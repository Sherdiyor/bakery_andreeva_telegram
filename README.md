# Bakery Andreeva Bot

## English

### Overview

The Bakery Andreeva Bot is a Telegram bot designed to assist the owner of the Bakery Andreeva web service in managing and processing orders efficiently. This bot provides a simple interface for viewing new orders and marking them as completed.

### Features

- **Order Notifications:** The bot notifies the admin about new orders received from customers.
- **Order Management:** Admin can view details of each order and mark them as completed.
- **User-Friendly Interface:** Easy navigation through inline buttons for quick actions.

### Setup

1. **Environment Variables:** 
   - Set up your .env file with the following variables:
     
     BOT_TOKEN=your_bot_token_here
     ADMIN_CHAT_ID=your_admin_chat_id_here
     
2. **Dependencies:**
   - Install the required packages:
     bash
     pip install python-telegram-bot python-dotenv
     
3. **Run the Bot:**
   - Execute the script:
     bash
     python main.py
     
### Usage

- Start the bot by sending the /start command in your Telegram chat.
- The bot will display the number of pending orders and provide a button to view them.
- Click on the order button to see details and mark orders as completed.

### Contributing

Feel free to contribute by forking the repository and submitting a pull request. Any improvements or bug fixes are welcome!

---

## Русский

### Обзор

Бот Пекарни Андреева — это Telegram-бот, созданный для помощи владельцу веб-сервиса Пекарня Андреева в эффективном управлении и обработке заказов. Этот бот предоставляет простой интерфейс для просмотра новых заказов и их отметки как выполненных.

### Функции

- **Уведомления о заказах:** Бот уведомляет администратора о новых заказах, полученных от клиентов.
- **Управление заказами:** Администратор может просматривать детали каждого заказа и отмечать их как выполненные.
- **Удобный интерфейс:** Легкая навигация через встроенные кнопки для быстрого доступа к действиям.

### Установка

1. **Переменные окружения:** 
   - Настройте свой файл .env со следующими переменными:
     
     BOT_TOKEN=ваш_токен_бота_здесь
     ADMIN_CHAT_ID=ваш_id_администратора_здесь
     
2. **Зависимости:**
   - Установите необходимые пакеты:
     bash
     pip install python-telegram-bot python-dotenv
     
3. **Запустите Бота:**
   - Выполните скрипт:
     bash
     python main.py
     
### Использование

- Начните работу с ботом, отправив команду /start в вашем чате Telegram.
- Бот отобразит количество ожидающих заказов и предоставит кнопку для их просмотра.
- Нажмите на кнопку заказа, чтобы увидеть детали и отметить заказы как выполненные.

### Участие

Не стесняйтесь вносить свой вклад, сделав форк репозитория и отправив запрос на слияние. Мы приветствуем любые улучшения или исправления ошибок!