class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self, increase=5000):
        if increase == 5000:
            self.salary += increase
            return self.salary
        else:
            self.salary += increase
            return self.salary


# em1 = Employee('Alex', 'Balduino', 2500)
# print(em1.give_raise())
# print(em1.give_raise(10000))
