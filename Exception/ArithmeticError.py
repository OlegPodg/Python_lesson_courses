try:
    k = 1 / 0
# except ZeroDivisionError:
except ArithmeticError:
    k = 0

print(k)
