class Calculator:

    def __init__(self):
        self.number_1 = float(input("Введите первое число (используйте точку для дробных чисел): "))
        self.number_2 = float(input("Введите второе число (используйте точку для дробных чисел): "))

    def add(self):
        result = self.number_1 + self.number_2
        return result

    def sub(self):
        result = self.number_1 - self.number_2
        return result

    def mult(self):
        result = self.number_1 * self.number_2
        return result

    def div(self):
        try:
            result = self.number_1 / self.number_2
            return result
        except ZeroDivisionError:
            result = 0
            print(f"Деление на {result}!")


x = Calculator()
x.div()
