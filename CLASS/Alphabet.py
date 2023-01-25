import string
""" 

"""

class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):  # Печатаем все буквы алфавита
        print(self.letters)

    def letters_num(self):  # Возвращаем количество букв в алфавите
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letter):  # Проверяем, относится ли буква к английскому языку
        if letter.upper() in self.letters:
            return True
        else:
            return False

    def letters_num(self):  # Возвращаем количество букв в алфавите
        return EngAlphabet.__letters_num

    @staticmethod  # Печатает пример текста на английском
    def example():
        print("Example: Whatever doesn't kill us makes us strong")


al = EngAlphabet()  # Создаем объект класса EngAlphabet
al.print()  # Выводим буквы алфавита для нашего объекта
print(al.letters_num())  # Выводим количество букв в алфавите
print(al.is_en_letter("F"))  # Проверяем, относится ли буква "F" к английскому языку
print(al.is_en_letter("Щ"))  # Проверяем, относится ли буква "Щ" к английскому язык
EngAlphabet.example()  # Выводим пример текста на английском

