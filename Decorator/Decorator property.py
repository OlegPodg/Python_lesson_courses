"""
Пример разработки класса Person
- ФИО
- возраст (целое число от 14 до 120)
- серия и номер паспорта в формате НН ХХХХХХХ, где Х - цифра (0-9), а H - буквы
- вес в кг. (вещественные числа от 20 и выше)
"""
from string import ascii_letters


class Person:
    s_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
    s_Rus_UPPER = s_RUS.upper()

    def __init__(self, fio, old, passport, weight):
        # Вызываем стат метод. Если произойдет хотя бы одно исключение, то программа остановится, если нет, то дальше
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(passport)
        self.verify_weight(weight)

        self.__fio = fio.split()  # ФИО должно быть списком
        self.__old = old
        self.__passport = passport
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        # переменная letters хранит все английские и русские буквы в ВЕРХНЕМ и нижнем регистре
        letters = ascii_letters + cls.s_RUS + cls.s_Rus_UPPER
        for s in f:
            # проверяем есть ли в нашей введенном ФИО хотя бы одна буква, если нет, вызываем исключение
            if len(s) < 1:
                raise TypeError("В ФИО должна быть хотя бы одна буква!")
            # длина всех удаленных элементов (то есть всех наших букв), должна быть равна 0, значит посторонних символов нет
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО должны использоваться только буквенные символы и дефис")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14 - 120]")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом и выше 20 кг")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 2 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        if not s[0].isalpha():  # Если в паспортные данные (серия) введены не буквы
            raise TypeError("Серия паспорта должна состоять из букв")
        if not s[1].isdigit():  # Если в паспортные данные (номер) введены не числа
            raise TypeError("Номер паспорта должен состоять из цифр")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)  # вызывается при передаче новых данных ВОЗРАСТА объекту для проверки перед записью
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)  # вызывается при передаче новых данных ВЕСА объекту для проверки перед записью
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)  # вызывается при передаче новых паспортных данных объекту для проверки перед записью
        self.__passport = ps


p = Person("Иванов Иван Иванович", 31, "МС 286525", 100.0)
p.old = 120
p.passport = "VC 263854"
p.weight = 90.0
print(p.__dict__)  # Выведем в консоль коллекцию dict, посмотрим какие локальные значения в итоге принимает
print(p.old)  # Прочитаем возраст нашего объекта класса
