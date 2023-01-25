import json

with open("data.json", encoding="UTF-8") as file:
    data = json.load(file)
print(data["email"])
print(data["surname"])
print(data["admin"])
print(data["friends"])