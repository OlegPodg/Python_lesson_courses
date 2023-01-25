import asyncio
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config  # импортируем файл config.py
import keyboard  # импортируем файл keyboard.py

import logging

"""----------------------------------настройка бота и логирование---------------------------------------------------"""

storage = MemoryStorage()  # FSM хранилище состояний
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)  # инициализируем бота
dispatch = Dispatcher(bot, storage=storage)  # инициализируем диспетчер к нашему боту и передаем хранилище состояний

logging.basicConfig(filename="log.txt",
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)

"""----------------------------------настройка FMS (хранилище состояний)--------------------------------------------"""


class InfoAboutMe(StatesGroup):
    Q1 = State()
    Q2 = State()


@dispatch.message_handler(Command("me"), state=None)  # Создаем команду /me для админа
async def enter_me_info(message: types.Message):
    # сверяем id пославшего сообщение с id админа
    if message.chat.id == config.admin:
        await message.answer("Начинаем настройку:\n"
                             "№1 Введите ссылку на ваш профиль")  # Бот спрашивает ссылку
        await InfoAboutMe.Q1.set()  # начинаем ждать наш ответ


@dispatch.message_handler(state=InfoAboutMe.Q1)  # Как только бот получит ответ, вот это выполнится
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text  # сохраняем текст полученного сообщения
    # тут запишется наша ссылка в виде словаря: ключ - "answer1", значение - наш записанный текст в answer
    await state.update_data(answer1=answer)

    await message.answer("Ссылка сохранена. \n"
                         "№2 Введите текст.")
    await InfoAboutMe.Q2.set()  # дальше ждем пока мы введем текст


@dispatch.message_handler(state=InfoAboutMe.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text  # сохраняем текст полученного сообщения
    # тут запишется наш текст Q2 в виде словаря: ключ - "answer2", значение - наш записанный текст в answer
    await state.update_data(answer2=answer)

    await message.answer("Текст сохранен.")

    data = await state.get_data()  # атрибут состояния содержит словарь из ключей answer1 и answer2

    answer1 = data.get("answer1")
    answer2 = data.get("answer2")

    with open("link.txt", 'w', encoding="UTF-8") as link_txt:
        # записываем строкой ссылку в наш файл
        link_txt.write(str(answer1))
    # открываем файл text.txt в режиме записи в той же кодировке
    with open("text.txt", "w", encoding="UTF-8") as text_txt:
        # записываем в файл текст, который передал пользователь
        text_txt.write(str(answer2))

    await message.answer(f"Ваша ссылка на профиль: {answer1}\nВаш текст: {answer2}")

    await state.finish()  # обязательно закрываем текущее состояние


""" -------------------------------------- обработка команды "/start" -----------------------------------------------"""


@dispatch.message_handler(commands="start", state=None)
# задаем функцию, которая отправит сообщение на заданную команду
async def welcome(message: types.Message):
    joined_file = open("user.txt", "r")  # создаем файл в которой будем записывать id пользователя
    joined_users = set()
    for line in joined_file:  # цикл в котором проверяем имеется ли такой id в файле user.txt
        joined_users.add(line.strip())

    if not str(message.chat.id) in joined_users:  # делаем запись в файл user.txt нового id
        joined_file = open("user.txt", "a")
        joined_file.write(str(message.chat.id) + "\n")
        joined_users.add(message.chat.id)
        # после проверки и записи выводим сообщение с именем пользователя и отображаем кнопки
    await bot.send_message(message.chat.id, f"Привет, *{message.from_user.first_name},* БОТ РАБОТАЕТ",
                           reply_markup=keyboard.start, parse_mode=types.ParseMode.MARKDOWN)


"""
-------------------------------------->>>> БЛОК КОДА ДЛЯ РАБОТЫ С РАССЫЛКОЙ<<<< ----------------------------------------
-----------В данной части рассмотрен хендлер для рассылки пользователем бота и отправка им фотографий-------------------
"""


@dispatch.message_handler(commands="sendpic")  # рассылка картинки
async def send_picture(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Рассылка началась "
                                                f"\nБот оповестит когда рассылку закончит*",
                               parse_mode=types.ParseMode.MARKDOWN)
        receive_users, block_users = 0, 0

        with open("user.txt", "r") as joined_file:
            joined_users = set()
            for line in joined_file:
                joined_users.add(line.strip())
            joined_file.close()
            for user in joined_users:
                try:
                    await bot.send_photo(user, open("photo.jpg", 'rb'))
                    receive_users += 1
                except:
                    block_users += 1
                await asyncio.sleep(0.4)
            await bot.send_message(message.chat.id, f"*Рассылка была завершена *\n"
                                                    f"получили сообщение: *{receive_users}*\n"
                                                    f"заблокировали бота: *{block_users}*",
                                   parse_mode=types.ParseMode.MARKDOWN_V2)


"""------------------------------------>>>> обработка команды "/links" <<<< ----------------------------------------"""


@dispatch.message_handler(commands="links")
async def send_picture(message):
    await bot.send_message(message.chat.id, text="*Полезные ссылки:*",
                           parse_mode="Markdown", reply_markup=keyboard.url_keyboard_button)


"""
------------------------->>>> БЛОК КОДА С ИНФОРМАЦИЕЙ И СТАТИСТИКОЙ и РАЗЗРАБОТЧИКОМ<<<< -------------------------------
Данная часть кода для работы с получением информации о пользователях.
Здесь расположены хендлеры для обработки команд "Информация", "Статистка" и "Разработчик".
"""

"""--------------------кнопка /Информация, /Статистика, /Разработчик и /Покажи пользователя--------------------------"""


@dispatch.message_handler(content_types="text")
# задаем функцию, которая отправит сообщение на заданную команду
async def cmd_text(message: types.Message):
    if message.text == "Информация":
        await bot.send_message(message.chat.id, text="Информация\n*Полезные ссылки:*",
                               parse_mode="Markdown", reply_markup=keyboard.url_keyboard_button)
    elif message.text == "Статистика":
        await bot.send_message(message.chat.id, text=f"Хочешь посмотреть статистику бота?", reply_markup=keyboard.stats,
                               parse_mode=types.ParseMode.MARKDOWN)

    elif message.text == "Разработчик":
        await bot.send_message(message.chat.id, text=f"Хочешь посмотреть кто разработчик?",
                               reply_markup=keyboard.question_for_user, parse_mode=types.ParseMode.MARKDOWN)

    elif message.text == "Покажи пользователя":
        await bot.send_message(message.chat.id, text=f"Показать id?",
                               reply_markup=keyboard.show_id, parse_mode=types.ParseMode.MARKDOWN)

    elif message.text == "Отправить фото":
        await bot.send_photo(message.chat.id, open("cat.jpg", 'rb'))

    else:
        await bot.send_message(message.from_user.id, text=f"Вы написали: {message.text}")


"""_______________________________________ОБРАБОТКА Inline-кнопок____________________________________________________"""

"""-------------------------------------обработка inline-кнопки "Да"-------------------------------------------------"""


@dispatch.callback_query_handler(text_contains='join')
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open("user.txt"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f"Вот статистика бота: *{d}* человек", parse_mode=types.ParseMode.MARKDOWN)

    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f"У тебя нет админки\n Куда ты полез", parse_mode=types.ParseMode.MARKDOWN)


"""---------------------------------------обработка inline-кнопки "Нет"----------------------------------------------"""


# задаем хендлер для команды cancel
# при этом входящий запрос должен содержать строку cancel
@dispatch.callback_query_handler(text_contains='cancel')
async def cancel(call: types.CallbackQuery):
    # говорим боту изменить сообщение
    # прописав путь до этого сообщения
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Ты вернулся в главное меню. Жми опять кнопки",
                                parse_mode=types.ParseMode.MARKDOWN)


"""-------------------------------обработка inline-кнопки "Показать разработчика"------------------------------------"""


@dispatch.callback_query_handler(text_contains='q_yes')
async def q_yes(call: types.CallbackQuery):
    link1 = open("link.txt", encoding="utf-8")
    link = link1.read()

    text1 = open("text.txt", encoding="utf-8")
    text = text1.read()
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Создатель: {link}\n{text}", parse_mode=types.ParseMode.HTML)


"""-----------------------------обработка inline-кнопки "Не показывать разработчика"---------------------------------"""


@dispatch.callback_query_handler(text_contains='q_no')
async def cancel(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Возврат в главное меню", parse_mode=types.ParseMode.MARKDOWN)


"""-----------------------------------обработка inline-кнопки "Хочу увидеть id"--------------------------------------"""


@dispatch.callback_query_handler(text_contains='show_yes')
async def cancel(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Вот твой ID: {call.message.chat.id}",
                                parse_mode=types.ParseMode.HTML)


"""-----------------------------------обработка inline-кнопки "Вернуться обратно"------------------------------------"""


@dispatch.callback_query_handler(text_contains="show_no")
async def cancel(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Вы отменили выбор", parse_mode=types.ParseMode.MARKDOWN)


"""----------------------------------------------------точка входа---------------------------------------------------"""
# Создаем точку входа
if __name__ == "__main__":
    # и запускаем нашего бота в режиме start_polling
    # по сути после этого во время работы нашего бота
    # бот будет постоянно получать и отвечать на сообщения
    print("Бот запущен!")
    executor.start_polling(dispatch, skip_updates=True)
