import unittest

from country_codes import get_country_code


class CountryCodesTestCase(unittest.TestCase):
    """Tests for country_codes.py."""

    def test_get_country_code(self):
        """Testa a função get_country_code()."""
        country_code = get_country_code('Andorra')
        self.assertEqual(country_code, 'ad')

        country_code = get_country_code('United Arab Emirates')
        self.assertEqual(country_code, 'ae')

        country_code = get_country_code('Tanzania')
        self.assertEqual(country_code, 'tz')

        country_code = get_country_code('Brazil')
        self.assertEqual(country_code, 'br')

        country_code = get_country_code('Afghanistan')
        self.assertEqual(country_code, 'af')


if __name__ == '__main__':
    unittest.main()
    