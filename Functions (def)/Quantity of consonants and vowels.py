import re

"""

Задача № 5.
Написать функцию, которая считает сколько гласных и согласных в строке.
Строку вводить с клавиатуры.


"""


def string_(user_str):
    count_vowels = len(re.findall(r'[уеыаоэяёию]', user_str.lower()))  # Считаем кол-во гласных в строке
    count_consonants = len(re.findall(r'[йцкнгшщзхфвпрлджчсмтб]', user_str.lower()))  # Считаем кол-во согласных
    print(f"Гласных в строке: {count_vowels}")  # Выводим на экран кол-во гласных в строке
    print(f"Согласных в строке: {count_consonants}")  # Выводим на экран кол-во согласных в строке


user_string = input("Введите строку: ")
string_(user_string)
