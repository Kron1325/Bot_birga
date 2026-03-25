import telebot
from telebot import types


bot = telebot.TeleBot('8737742382:AAEI84XHh4AhVASDOBiUF_Ku7lk7SrYvpwg')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Хочу узнать про проект")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Здравствуйте, это FAQ бот для проекта WealthWise. Выберите что вас интерисует", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Хочу узнать про проект':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Видео проекта')
        btn2 = types.KeyboardButton('Команда')
        btn3 = types.KeyboardButton('Фин.модель')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Видео проекта':
        bot.send_message(message.from_user.id, 'Бекенд веб приложения(без фронта) ' + 
                         '[ссылке](https://drive.google.com/file/d/12xU4THUMgJWzpuunyUbEnO9PIXM2a2Eg/view?usp=sharing)', 
                         parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Фронтенд веб приложения(без фронта) ' + 
                         '[ссылке](https://drive.google.com/file/d/1HYO0posLiK3-McX83tg8xn7M2QkHWc5N/view?usp=sharing)', 
                         parse_mode='Markdown')


                         
    elif message.text == 'Команда':
        bot.send_message(message.from_user.id, 'Тут представлена наша команда: ') 
        photo_path_1 = 'img/sergei.png'
        bot.send_photo(message.chat.id, open(photo_path_1, 'rb'))
        bot.send_message(message.from_user.id, 'Карцев Сергей: Тим лид, аналитик, бекенд разработчик ' \
        '@Deepsfakese', parse_mode='Markdown')
        photo_path_2 = 'img/semen.png'
        bot.send_photo(message.chat.id, open(photo_path_2, 'rb'))
        bot.send_message(message.from_user.id, 'Нехорошков Семён: UX/UI дизайнер, фронтенд разработчик, аналитик ' \
        '@Crimes78', parse_mode='Markdown')


    elif message.text == 'Фин.модель':
        bot.send_message(message.from_user.id, 'Наша финансовая модель ' + 
                         '[ссылке](https://docs.google.com/spreadsheets/d/1C7eGBYpBwL6Q4tANm8MU1_Rp4UNkhgY85L6Y_JtuNOk/edit?gid=1153874955#gid=1153874955)', 
                         parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть  
