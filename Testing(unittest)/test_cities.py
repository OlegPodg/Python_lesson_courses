import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country('santiago', 'china'), 'Santiago, China')

    def test_city_country_population(self):
        self.assertEqual(city_country('santiago', 'china', '5000000'), 'Santiago, China - population 5000000')


if __name__ == '__main__':
    unittest.main()
