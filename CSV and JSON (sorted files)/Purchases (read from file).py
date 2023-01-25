import json

"""
Домашнее задание.
Задача №2.
Прочитав файл "purchase.json" из предыдущего задания и вывести стоимость всех покупок за день.

"""


def all_cost_user_purchase():  # Объявляем функцию all_cost_user_purchase
    with open("purchase.json", 'r', encoding="utf-8") as file:  #
        data = json.load(file)  # Считываем файл purchase.json
    count = 0  # Создаем счетчик для подсчета стоимости всех покупок за день
    for i in data:  # Запускаем цикл по списку в файле
        for value in i.values():  # Запускаем цикл по словарю (элемент списка), и возвращаем значение
            if value.isdigit():  # Если значение является числом, то
                count += int(value)  # Добавляем значение в счетчик преобразуя значение в число
    return count  # Возвращаем счетчик для подсчета стоимости всех покупок за день


print(f"Стоимость всех покупок за день: {all_cost_user_purchase()}")  # Вызываем функцию
