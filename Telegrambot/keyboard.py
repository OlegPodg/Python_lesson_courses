from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основа для кнопок

info = types.KeyboardButton("Информация")  # кнопка информации
statistics = types.KeyboardButton("Статистика")  # кнопка статистики
developer = types.KeyboardButton("Разработчик")  # кнопка разработчик
info_users = types.KeyboardButton("Покажи пользователя")
send_photo = types.KeyboardButton("Отправить фото")
start.add(statistics, info)  # добавить кнопки в основу бота
start.add(developer, info_users)
start.add(send_photo)

stats = InlineKeyboardMarkup()  # создаем основу для инлайн кнопок
stats.add(InlineKeyboardButton("Да", callback_data="join"))  # создаем кнопку и колбэк к ней
stats.add(InlineKeyboardButton("Нет", callback_data="cancel"))  # создаем кнопку и колбэк к ней

question_for_user = InlineKeyboardMarkup()
question_for_user.add(InlineKeyboardButton("Показать разработчика", callback_data="q_yes"))
question_for_user.add(InlineKeyboardButton("Не показывать разработчика", callback_data="q_no"))

show_id = InlineKeyboardMarkup()
show_id.add(InlineKeyboardButton("Хочу увидеть id", callback_data="show_yes"))
show_id.add(InlineKeyboardButton("Вернуться обратно", callback_data="show_no"))

url_keyboard_button = InlineKeyboardMarkup(row_width=1)
url_keyboard_button_1 = InlineKeyboardButton(text='Перейти на сайт Моя IT Школа', url='https://myitschool.by/')
url_keyboard_button_2 = InlineKeyboardButton(text='Перейти на Курс по Python разработке',
                                             url='https://myitschool.by/kursy-it/razrabotka-veb-prilozhenij-na-python/')
url_keyboard_button.add(url_keyboard_button_1, url_keyboard_button_2)
