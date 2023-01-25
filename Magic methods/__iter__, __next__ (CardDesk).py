"""
Домашнее задание.
Реализуйте итератор колоды карт (52 штуки) CardDesk.
Каждая карта представлена в виде строки типа "2 Пик".
При вызове функции next() будет представлена следующая карта.
По окончании перебора всех элементов возникнет ошибка StopIteration.
"""


class CardDesk:
    ACE = "Туз"  # Static attribute
    KNAVE = "Валет"  # Static attribute
    QUEEN = "Дама"  # Static attribute
    KING = "Король"  # Static attribute

    def __init__(self, start=1, stop=14, step=1):
        self.start = start  # Dynamic attribute
        self.stop = stop  # Dynamic attribute
        self.step = step  # Dynamic attribute

    def __iter__(self):  # Magic method
        self.value = self.start - self.step
        return self

    def __next__(self):  # Magic method
        if self.value + self.step < self.stop:
            self.value += self.step
            if self.value == 1:  # If self.value is equal to 1, then return self.ACE ("Туз")
                return self.ACE
            elif self.value == 11:  # If self.value is equal to 11, then return self.KNAVE ("Валет")
                return self.KNAVE
            elif self.value == 12:  # If self.value is equal to 12, then return self.QUEEN ("Дама")
                return self.QUEEN
            elif self.value == 13:  # If self.value is equal to 13, then return self.KING ("Король")
                return self.KING
            else:
                return self.value  # else, then return self.value
        else:
            raise StopIteration  # Raise an exception


player = CardDesk()  # Instance of the class is created
list_card_suit = ["Пик", "Бубна", "Черви", "Треф"]  # Created a list with card suit elements
for y in list_card_suit:  # Starts a cycle for sorting card suits
    for i in player:  # Starts a nested cycle for instance of the class (using magic methods)
        print(f"{i}-{y}", end=" ")
    print()


