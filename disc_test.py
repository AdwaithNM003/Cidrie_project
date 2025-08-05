import unittest
from calc_disc import calculate_discount
class TestingDisc(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_discount(100,30),70)
    def test_price0(self):
        self.assertEqual(calculate_discount(0,100),0)
    def test_priceneg(self):
        with self.assertRaises(ValueError):
            calculate_discount(-21,100)
            print(ValueError)
    def test_percentage110(self):
        with self.assertRaises(ValueError):
            calculate_discount(120,110)
            print(ValueError)
    def test_percentageneg(self):
        with self.assertRaises(ValueError):
            calculate_discount(120,-25)
            print(ValueError)
if __name__ == '__main__':
    unittest.main()