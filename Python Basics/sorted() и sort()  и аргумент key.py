# list.sort() - метод для сортировки элементов списка
# sorted() - функция для сортировки итерируемых объектов.

list_1 = [1, -5, -150, 25, -3, 14]
list_1.sort()
print(list_1)

print(sorted(list_1))
print(sorted(list_1, reverse=True))

# Сортировка словарей
d = {1: "one", 2: "two", 4: "four", 3: "tree"}
print(sorted(d))
print(sorted(d.values()))
print(sorted(d.items()))

# _________________________________________________

list_2 = [1, -5, -150, 25, -3, 14, "hi", "one"]

print(sorted(list_2, key=str))