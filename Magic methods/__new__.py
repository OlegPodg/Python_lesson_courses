class Something:
    # переопределяем метод __new__, в котором обязательно делаем ссылку на текущий класс,
    # также указываем на прием неограниченного количества позиционных и ключевых аргументов

    def __new__(cls, *args, **kwargs):
        print(f"сработал __new__ для класса {cls.__name__}, переданы аргументы: {args, kwargs}")

        # теперь мы к примеру, решили на этапе создания объекта добавить
        # новый атрибут, для этого мы переопределяем __new__ родителя(object)
        instance = super().__new__(cls)

        # добавляем к экземпляру новый атрибут
        instance.new_attribute = "добавлено"

        # в результате работы функции мы должны вернуть объект
        # в нашем случае instance (новый объект)
        return instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


example = Something("Igor", 24)
print(example.__dir__())
