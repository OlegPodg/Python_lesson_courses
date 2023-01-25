import json

"""
Домашнее задание.
Задача №1.
Пользователь будет вводить название и стоимость каждой своей покупки за день, до тех пор пока он не напишет
"стоп". Ваша задача записать это в json файл в формате:
{"название":"яблоко",
 "стоимость":"200"}

"""

user_purchase = []  # Создаем пустой список для покупок


def user_input():  # Объявляем функцию user_input
    while True:  # Запускаем цикл
        # Запрос от пользователя на ввод название продукта ('стоп' для выхода)
        str_name = input("Введите название продукта (введите 'стоп', если хотите закончить):")
        if str_name.lower() == 'стоп':  # Если ввели 'стоп', то останавливаем цикл
            break
        # Запрос от пользователя на ввод стоимости продукта
        str_cost = input("Введите стоимость продукта:")
        # Добавление в список user_purchase словаря
        user_purchase.append({"название": str_name.lower(), "стоимость": str_cost})
    return user_purchase  # Возвращаем список user_purchase


# Открываем наш файл purchase.json и записываем список user_purchase в формате json
with open("purchase.json", "w", encoding="UTF-8") as file:
    json.dump(user_input(), file, ensure_ascii=False)