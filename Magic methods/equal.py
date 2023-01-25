class Word(str):  # Класс для слов, определяющий сравнение по длине слов.
    def __new__(cls, word):
        if " " in word:
            # Если
            word = word[:word.index(" ")]  # Теперь в word это все символы до первого пробела

        return str.__new__(cls, word)

    def __gt__(self, other):  # определяем поведение оператора >
        return len(self) > len(other)

    def __lt__(self, other):  # определяем поведение оператора <
        return len(self) < len(other)

    def __ge__(self, other):  # определяем поведение оператора >=
        return len(self) >= len(other)

    def __le__(self, other):  # определяем поведение оператора <=
        return len(self) <= len(other)


example = Word("Один два")
print(example > "два")
print(example < "два")
print(example == "два")
print(example != "два")
