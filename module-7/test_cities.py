import unittest

from city_functions import city_country_function

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        result = city_country_function("Santiago","Chile")
        self.assertEqual(result, "Santiago, Chile")
if __name__ == '__main__':
    unittest.main() 