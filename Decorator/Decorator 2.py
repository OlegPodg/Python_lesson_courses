"""
Напишите декоратор debug, который при каждом вызове декорируемой функции выводит:
 - ее имя (вместе со всеми передаваемыми аргументами);
 - какое значение она возвращает;
 - после этого выводится результат ее выполнения
"""

import logging

logging.basicConfig(filename="logging_lesson19.log",
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(funcName)s || %(message)s")


def debug(func):  # Function decorator
    def wrapper(num_1, num_2):  # Function that takes two positional arguments
        # When the decorated function is launched, we write to the log file about the successful start
        logging.info(f"Function {func.__name__} started ")
        res = func(num_1, num_2)
        logging.info(f"Function {func.__name__} finished ")
        print(f"Run function: {func.__name__}, with params: {num_1, num_2}")
        print(f"Function result: {res}")
        return res  # The result of the function func_dec

    return wrapper  # Function reference call


@debug
def func_dec(num1, num2):  # Decorated function
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as zdO:
        logging.error(zdO)  # If a divide-by-zero exception is triggered, then we write to the log file
    except TypeError as te:
        logging.exception(te)  # If a data type error exception is triggered, then we write to the log file


print(func_dec(25, 55))  # function call
print(func_dec(45, 0))  # function call
print(func_dec(150, "zero"))  # function call
