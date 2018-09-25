from unittest import TestCase, mock

from pricer import Pricer


class TestClassAttribute(TestCase):

    def test_patch_class_attribute(self):
        with mock.patch.object(Pricer, 'DISCOUNT', 1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

        self.assertAlmostEqual(pricer.get_discounted_price(100), 80)

    def test_patch_class_attribute_with_path(self):
        with mock.patch('pricer.Pricer.DISCOUNT', 1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

        self.assertAlmostEqual(pricer.get_discounted_price(100), 80)

    def test_patch_instance_attribute(self):
        pricer = Pricer()
        pricer.DISCOUNT = 0.5
        self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

    def test_set_class_attribute(self):
        Pricer.DISCOUNT = 0.75
        pricer = Pricer()
        self.assertAlmostEqual(pricer.get_discounted_price(100), 75.0)