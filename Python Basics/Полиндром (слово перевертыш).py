#  Первый способ использовать split и join
string_ = "леша на полке клопа нашел"
string_new = "".join(string_.split())
print(string_new)
print(string_new == string_new[::-1])


#  Второй способ использовать метод .replace()
string_ = "а роза упала на лапу азора"
string_new = string_.replace(' ', '')
print(string_new)
print(string_new == string_new[::-1])

