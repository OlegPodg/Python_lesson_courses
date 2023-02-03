import unittest
from increase_salary import Employee


class TestSalaryEmployee(unittest.TestCase):

    def setUp(self):
        self.test_salary = Employee('Holand', 'Braut', 25000)

    def test_give_default_raise(self):
        self.assertEqual(self.test_salary.give_raise(), 30000)

    def test_give_custom_raise(self):
        self.assertEqual(self.test_salary.give_raise(10000), 35000)


if __name__ == '__main__':
    unittest.main()
