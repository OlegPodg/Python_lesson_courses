# Совершенное число — это положительное целое число, равное сумме его положительных делителей (не считая само число).
# Например, 6 — совершенное число, потому что 6 = 1 + 2 + 3


def perfect_number(num):
    return sum([i for i in range(1, num) if num % i == 0]) == num

number_per = int(input("Введите число: "))
print(perfect_number(number_per))