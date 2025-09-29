# test_shipping_final.py

import unittest
from dynamic_shipping import calculate_shipping_fee

class TestSingleBoundaryFinal(unittest.TestCase):
    def test_1_orderValue_min_minus(self):
        with self.assertRaises(ValueError):
            calculate_shipping_fee(-1000, 10, "THUONG", False)

    def test_2_orderValue_min(self):
        self.assertAlmostEqual(calculate_shipping_fee(0, 10, "THUONG", False), 30000)

    def test_3_orderValue_min_plus(self):
        self.assertAlmostEqual(calculate_shipping_fee(1000, 10, "THUONG", False), 30000)

    def test_4_orderValue_norm(self):
        self.assertAlmostEqual(calculate_shipping_fee(300000, 10, "THUONG", False), 30000)

    def test_5_orderValue_max(self):
        self.assertAlmostEqual(calculate_shipping_fee(500000, 10, "THUONG", False), 0)

    def test_6_distance_min_minus(self):
        with self.assertRaises(ValueError):
            calculate_shipping_fee(300000, -0.1, "THUONG", False)

    def test_7_distance_min(self):
        with self.assertRaises(ValueError):
            calculate_shipping_fee(300000, 0, "THUONG", False)

    def test_8_distance_min_plus(self):
        self.assertAlmostEqual(calculate_shipping_fee(300000, 0.1, "THUONG", False), 20000)
    def test_9_distance_max_minus(self):
        self.assertAlmostEqual(calculate_shipping_fee(300000, 19.9, "THUONG", False), 44850)

    def test_10_distance_max(self):
        self.assertAlmostEqual(calculate_shipping_fee(300000, 20, "THUONG", False), 45000)

    def test_11_distance_max_plus(self):
        with self.assertRaises(ValueError):
            calculate_shipping_fee(300000, 20.1, "THUONG", False)

    def test_12_customerType_vip(self):
        self.assertAlmostEqual(calculate_shipping_fee(300000, 10, "VIP", False), 0)
    def test_13_customerType_moi(self):
        self.assertAlmostEqual(calculate_shipping_fee(300000, 10, "MOI", False), 0)
    
    def test_14_isOversized_false(self):
        self.assertAlmostEqual(calculate_shipping_fee(300000, 10, "THUONG", False), 30000)

if __name__ == '__main__':
    unittest.main(verbosity=2)