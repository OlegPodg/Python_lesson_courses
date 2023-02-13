# Задание №6
# Таблица умножения от 1 до 9

# Первый способ
print("Выводим таблицу умножения от 1 до 9")
count = 0
for i in range(1, 10):
    for a in range(1, 10):
        count = i * a
        print(f"{a} * {i} = {count}", end="\t\t")
    print("\n")

# Второй способ

print("Выводим таблицу умножения от 1 до 9")
count = 0
for i in range(1, 10):
    for a in range(1, 2):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(2, 3):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(3, 4):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(4, 5):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(5, 6):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(6, 7):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(7, 8):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(8, 9):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}", end="     ")
        else:
            print(f"{a} * {i} = {count}", end="      ")
    for a in range(9, 10):
        count = i * a
        if count >= 10:
            print(f"{a} * {i} = {count}")
        else:
            print(f"{a} * {i} = {count}")
