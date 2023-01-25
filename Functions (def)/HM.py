import re
import random

"""

Задание № 6.
Функцию, которая при заданном целом числе n подсчитает n + nn + nnn

"""


def sum_n(n):
    nn = n * n
    nnn = n * n * n
    return n + nn + nnn


num = int(input("Введите число n: "))
print(f"Результат n+n*n+n*n*n = {sum_n(num)}")

"""

Задание № 7.
Вычислить значения нижеприведенной функции в диапазоне значений х от -10 до 10
включительно с шагом, равным 1.

Вычисление значения функции оформить в виде программной функции, которая принимает
значение х, а возвращает полученное значение функции (у).

"""


def func_xy(x: int):
    if -5 <= x <= 5:
        y = x ** 2
        return y
    elif x < -5:
        y = 2 * abs(x) - 1
        return y
    else:
        y = 2 * x
        return y


a = random.randint(-10, 10)
print(f"x: {a}, y: {func_xy(a)}")

"""
Домашнее задание.
Если в функцию передаётся кортеж, то посчитать длину его слов.
Если список, то посчитать кол-во букв и чисел в нём.
Число - кол-во нечётных цифр.
Строка - кол-во букв.
Сделать проверку со всеми этими случаями.

"""


def tuple_(user_choice):  # Объявляем функцию tuple_ и передаем параметр user_choice
    count = 0  # создаем счетчик для подсчета длины слов
    for i in list(user_choice):
        if isinstance(i, str):  # Проверяем принадлежность элемента к типу данных строки
            count += len(i)  # Если условие выполнено, то в счетчик добавляем длину элемента
    return count  # Возвращает длину слов


def list_(user_choice):  # Объявляем функцию list_ и передаем параметр user_choice
    str_ = "".join(map(str, user_choice))  # Преобразуем список в строку
    len_isalpha = len([i for i in str_ if i.isalpha()])  # Находим буквы и подсчитываем их
    len_isdigit = len([i for i in str_ if i.isdigit()])  # Находим цифры и подсчитываем их
    return len_isalpha, len_isdigit  # возвращаем количество букв и цифр


def int_(user_choice):  # Объявляем функцию int_ и передаем параметр user_choice
    count = 0  # создаем счетчик для подсчета нечётных цифр
    for i in list(str(user_choice)):
        i = int(i)
        if i % 2 != 0:  # Если цифра нечетная, то добавляем в счетчик
            count += 1
    return count  # возвращаем кол-во нечетных цифр


def string_(user_choice):  # Объявляем функцию string_ и передаем параметр user_choice
    len_isalpha = len([i for i in user_choice if i.isalpha()])  # Находим буквы и подсчитываем их
    return len_isalpha  # Возвращает количество букв


tuple_choice = (1, 2, "один", "два", "три", 25)  # Создаем кортеж
list_choice = [23, 58, "hello", "bye", 96954]  # Создаем список
int_choice = 2536478912356  # Создаем число
string_choice = "Начинать всегда стоит с того, что сеет сомнения"  # Создаем строку

while True:
    # Запрос от пользователя
    user_input = int(input("Введите число типа данных, где "
                           "1 - кортеж, 2 - список, 3 - число, 4 - строка, 0 - для выхода:"))
    if user_input == 0:  # Выход
        break
    elif user_input == 1:  # Выбран кортеж
        print(f"Вы выбрали кортеж {tuple_choice}, длина всех его слов: {tuple_(tuple_choice)}")
    elif user_input == 2:  # Выбран список
        print(f"Вы выбрали список {list_choice}, количество букв и чисел: {list_(list_choice)}")
    elif user_input == 3:  # Выбран число
        print(f"Вы выбрали число {int_choice}, количество нечётных цифр: {int_(int_choice)}")
    elif user_input == 4:  # Выбрана строка
        print(f"Вы выбрали строку '{string_choice}', количество букв в строке: {string_(string_choice)}")
    else:
        print("Вы ввели некорректное число!")  # Введено некорректное число
