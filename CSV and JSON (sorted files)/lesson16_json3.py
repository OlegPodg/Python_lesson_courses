import json

data = {"id": 765, "email": "ivanov@mail.ru", "surname": "Иванов", "age": 45, "admin": False,
        "friends": [123, 456, 789]}
# преобразуем словарь в json-строку
# string = json.dumps(data)
# print(string)
# преобразуем словарь в json-строку
string = json.dumps(data, ensure_ascii=False)
print(string)