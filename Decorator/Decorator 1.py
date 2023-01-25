"""
Задача:
1. Дан список [ [1,2,3], [4, 5, 6], [7, 8, 9] ]
2. Напишите функцию, которая возвращает новый список, состоящий из
значений кратных 3.
3. Напишите декоратор, который будет возвращать количество значений,
не кратных 3 из вашей функции.

"""


def not_multiple_of_three(func):
    def wrapper(list_a):
        res = func(list_a)
        print(f"The result of the {func.__name__} function: list of elements divisible by 3 - {res}")
        res_2 = [y for i in list_a for y in i if y % 3 != 0]
        print(f"The result: list of elements not divisible by 3 - {res_2}")
        return len(res_2)

    return wrapper


@not_multiple_of_three
def multiple_of_three(list_):
    items_multiple_of_three = [y for i in list_ for y in i if y % 3 == 0]
    return items_multiple_of_three


list_all = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multiple_of_three(list_all))
