# <-- устанавливаем библиотеки -->

import time # Библиотека времени (для установки задержек)
import telebot # Библиотека для работы с тг ботами
import webbrowser # Библиотека для открытия ссылок в браузере

from telebot import types # Импортируем функцию types для работы с разными типами данных
bot = telebot.TeleBot('') # Нужно указать токен для бота


@bot.message_handler(commands=['start']) #При получении сообщения "start" вызывается функция -start-
def start(message):

    bot.send_message(message.chat.id, 'Привет я твой столовка бот, я создан для того'
    ' чтобы ты знал, что сегодня будут давать в столовой') # При вызове функции отправляется сообщение 

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # Подготавливаем кнопки для работы (устанаволиваем размер)

    button = types.KeyboardButton('Сегодня')  
    button1 = types.KeyboardButton('Завтра') 
    button2 = types.KeyboardButton('На сайт гимназии') 

    # <-- Положение кнопок в боте -->
    markup.add(button, button1) 
    markup.add(button2)

    time.sleep(2) # Задержка 2 секунды

    bot.send_message(message.chat.id, 'Выберите день: ', reply_markup=markup) # Отправляем сообщение перед выбором кнопки 


def starter(message): # Функция возврата (при нажатии на кнопку "Назад ↩️" вызывается эта функция)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # Подготавливаем кнопки для работы (устанаволиваем размер)

    button = types.KeyboardButton('Сегодня')
    button1 = types.KeyboardButton('Завтра')
    button2 = types.KeyboardButton('На сайт гимназии')

    # <-- Положение кнопок в боте -->
    markup.add(button, button1)
    markup.add(button2)

    time.sleep(2) # Задержка 2 секунды

    bot.send_message(message.chat.id, 'Выберите день: ', reply_markup=markup) # Отправляем сообщение перед выбором кнопки 

@bot.message_handler(content_types=['text']) # Обрабатываем текстовый вид сообщений (результаты нажатия кнопок)
def obrabotka(message):
    if message.text == 'Сегодня': # Если была нажата кнопка "Сегодня" выполняются след. команды
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # Подготавливаем кнопки для работы (устанаволиваем размер)

        button1 = types.KeyboardButton('Обед 🍲')
        button2 = types.KeyboardButton('Завтрак 🧆')
        button3 = types.KeyboardButton('Назад ↩️')

        # <-- Положение кнопок в боте -->
        markup.add(button1, button2)
        markup.add(button3)

        bot.send_message(message.chat.id, 'Выберите рацион 🍱', reply_markup=markup) # Отправляем сообщение перед выбором кнопки 

    elif message.text == 'Обед 🍲': # Если была нажата кнопка "Обед" выполняются след. команды
        bot.send_photo(message.chat.id, 'https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663686606_11-'
        'mykaleidoscope-ru-p-borshch-so-smetanoi-oboi-15.jpg') # Отправляем фотографию блюда

        time.sleep(0.4) # Задержка 0,4 секунды

        bot.send_message(message.chat.id, 'Описание:\n'
        '1. Суп - Густой сытный борщ\n'
        '2. Горячее - Азиатская лапша с говядиной\n'
        '3. Напиток - Морс лесные ягоды\n'
        '4. Хлеб рженой\n'
        '5. Яблоко')

    elif message.text == 'Завтрак 🧆': # Если была нажата кнопка "Завтрак" выполняются след. команды
        bot.send_photo(message.chat.id, 'https://simf-klin-bolnica.ru/wp-content/uploads/4/e/a/4ea2d461fe'
        '1a11f795cbd9d8a523f9c6.jpeg') # Отправляем фотографию блюда

        time.sleep(0.4) # Задержка 0,4 секунды

        bot.send_message(message.chat.id, 'Описание:\n'
        '1. Овсяная каша на молоке с ягодами\n'
        '2. Хлеб - батон\n'
        '3. Напиток - Древесный чай с кусочками лимона\n'
        '4. Банан')

    elif message.text == 'Назад ↩️': # Если была нажата кнопка "Назад" выполняются след. команды
        starter(message) # Вызываем функцию "starter()" - возвращает на главную

    elif message.text == 'Завтра': # Если была нажата кнопка "Завтра" выполняются след. команды
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # Подготавливаем кнопки для работы (устанаволиваем размер)
        button1 = types.KeyboardButton('Обед 🍲')
        button2 = types.KeyboardButton('Завтрак 🧆')
        button3 = types.KeyboardButton('Назад ↩️')

        # <-- Положение кнопок в боте -->
        markup.add(button1, button2)
        markup.add(button3)

        bot.send_message(message.chat.id, 'Выберите рацион 🍱', reply_markup=markup) # Отправляем сообщение перед выбором кнопки 

    elif message.text == 'На сайт гимназии': # Если была нажата кнопка "На сайт гимназии" выполняются след. команды
        webbrowser.open('https://гимназия47.екатеринбург.рф') # Если пользователь на пк то открывается сайт гимназии в браузере
        bot.send_message(message.chat.id, 'https://гимназия47.екатеринбург.рф') # бот отправляет ссылку на сайт гимназии


bot.polling(none_stop=True) # Позволяет не прекращать работу бота
