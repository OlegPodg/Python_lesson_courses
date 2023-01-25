# Задание 1
my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except KeyError:
    print("Ключа не существует!")

my_list = [1, 2, 3, 4, 5]

try:
    my_list[6]
except IndexError:
    print("Этого индекса нет в списке!")

# Задание 2
my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except IndexError:
    print("Такого индекса не существует!")
except KeyError:
    print("Этого ключа нет в словаре!")
except:
    print("Произошла другая ошибка!")

# Задание 3
my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except KeyError:
    print("Произошла ошибка KeyError!")
else:
    print("Ошибок не обнаружено!")
finally:
    print("Оператор finally выполнен!")
