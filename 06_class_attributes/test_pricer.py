from unittest import TestCase, mock, expectedFailure

from pricer import Pricer


class TestClassAttribute(TestCase):

    def test_patch_instance_attribute(self):
        pricer = Pricer()
        pricer.DISCOUNT = 0.5
        self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

    def test_set_class_attribute(self):
        Pricer.DISCOUNT = 0.75
        pricer = Pricer()
        self.assertAlmostEqual(pricer.get_discounted_price(100), 75.0)

    def test_patch_incorrect_class_attribute(self):
        with self.assertRaises(AttributeError):
            with mock.patch.object(Pricer, 'PERCENTAGE', 1):
                pass

    def test_patch_class_attribute(self):
        with mock.patch.object(Pricer, 'DISCOUNT', 1):
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

        self.assertAlmostEqual(pricer.get_discounted_price(100), 80)
