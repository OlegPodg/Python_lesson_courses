# Есть 2 способа сортировать списка в списке.

"""
1 способ.
Использовать функцию itemgetter() вместе с функцией sorted().
Нужно импортировать библиотеку itemgetter.
Можно использовать reverse=True - по убыванию
"""
from operator import itemgetter

list_1 = [[10, 8, 'Cat'], [90, 2, 'Dog'], [45, 6, 'Bird']]
print("itemgetter", sorted(list_1, key=itemgetter(0)))  # По возрастанию. По индексу 0, то есть 10, 45, 90
print("itemgetter (reverse):", sorted(list_1, key=itemgetter(0), reverse=True))  # По убыванию. По индексу 0: 90, 45, 10

"""
2 способ.
Использовать выражение lambda вместе с функцией sorted(). Можно и кортеж
"""
list_2 = [('john', 'A', 15),
          ('jane', 'B', 12),
          ('dave', 'B', 10)]
print("lambda:", sorted(list_2, key=lambda x: x[-1]))  # По возрастанию. По индексу 2, то есть по числам 10, 12, 15

"""
3 способ.
Для сортировки данного списка по длине ВНУТРЕННЕГО списка используется параметр key=len и метод sort
"""
list_3 = [[5, 90, 'Hi', 66], [80, 99], [56, 32, 80]]
list_3.sort(key=len)
print("Сортировка по длине элементов", list_3)

"""
Задание.
Файл содержит числа и буквы. Каждый записан в отдельной строке.
Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
а потом слова по возрастанию их длины

"""


def list_with_int_and_str():  # Объявляем функцию
    with open("example_lesson15_2.txt") as ex2:
        list_4 = ex2.read().split('\n')  # разбиваем строку на части (\n - перенос строк), и возвращаем в виде списка
        list_digit = []  # Создаем пустой словарь для чисел
        list_alpha = []  # Создаем пустой словарь для букв
        for i in list_4:  # Запускаем цикл по списке list_1
            if i.isdigit():  # Если элемент состоит из цифр, то
                list_digit.append(i)  # добавляем элемент в список list_digit
            else:  # Если элемент состоит из букв, то list_alpha
                list_alpha.append(i)  # добавляем элемент в список
    # возвращаем сортировку списков
    return sorted(list_digit, key=lambda x: int(x)) + sorted(list_alpha, key=len)


print(list_with_int_and_str())  # Вызываем функцию
