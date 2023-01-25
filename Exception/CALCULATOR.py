def calculator(num1: float, num2: float):
    while True:
        math_or_exit_operation = input("Введите необходимую операцию:\n+ ; - ; * ; / ; & (exit): ")
        if math_or_exit_operation == "&":
            print("До свидания!")
            break
        elif math_or_exit_operation == "+":
            add(num1, num2)
        elif math_or_exit_operation == "-":
            sub(num1, num2)
        elif math_or_exit_operation == "*":
            mult(num1, num2)
        elif math_or_exit_operation == "/":
            div(num1, num2)


def add(num1: float, num2: float):
    result = num1 + num2
    print(result)


def sub(num1: float, num2: float):
    result = num1 - num2
    print(result)


def mult(num1: float, num2: float):
    result = num1 * num2
    print(result)


def div(num1: float, num2: float):
    try:
        result = num1 / num2
        print(result ** 2)  # Результат если не ноль, то результат возвести в квадрат
    except ZeroDivisionError:
        result = 0
        print(f"Деление на {result}!")
    finally:
        print("Подсчет окончен.")


number_1 = float(input("Введите первое число (используйте точку для дробных чисел): "))
number_2 = float(input("Введите второе число (используйте точку для дробных чисел): "))

calculator(number_1, number_2)
