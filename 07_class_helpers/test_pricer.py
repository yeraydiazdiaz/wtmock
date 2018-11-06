from unittest import TestCase, mock, expectedFailure
from pricer import CountryPricer


class TestCountryPrices(TestCase):

    @expectedFailure
    def test_patch_constant(self):
        with mock.patch('pricer.COUNTRIES', ['GB']):
            pricer = CountryPricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)

    def test_patch_class_helper(self):
        with mock.patch('pricer.CountryPricer.country.default', 'GB'):
            pricer = CountryPricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)

        pricer = CountryPricer()
        self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 100)