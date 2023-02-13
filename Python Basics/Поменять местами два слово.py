# Поменять местами два введенных слова и заменить "1" на "one"

str_ = input("Введите два слова: ")  # запрос к пользователю ввести 2 слова
str_new = str_.find(' ')  # находим индекс пробела между введенными словами
# меняем местами слова (+1 используем, чтобы захватить пробел)
str_change_word_order = str_[str_new + 1:] + " " + str_[:str_new]
print(str_change_word_order)  # выводим на экран слова поменявшиеся местами
print(str_change_word_order.replace('1', 'one'))  # заменяем '1' на 'one'

"""
str_ = input("Введите два слова: ")
str_new = ' '.join(str_.split(' ')[::-1])
print(str_new)
print(str_new.replace('1', 'one'))
"""


