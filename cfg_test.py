
import unittest
from dynamic_shipping import calculate_shipping_fee

class TestShippingFeeBranchCoverage(unittest.TestCase):

    def test_09(self):
        order_value, distance, customer_type, is_oversized = (100000, 15, "VIP", False)
        self.assertAlmostEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 26250.0)

    def test_08(self):
        order_value, distance, customer_type, is_oversized = (600000, 8, "THUONG", False)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 0.0)

    def test_07(self):
        order_value, distance, customer_type, is_oversized = (350000, 4, "VIP", False)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 0.0)

    def test_06(self):
        order_value, distance, customer_type, is_oversized = (100000, 4, "THUONG", False)
        self.assertAlmostEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 20000.0)

    def test_05(self):
        order_value, distance, customer_type, is_oversized = (100000, 10, "MOI", False)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 0.0)

    def test_04(self):
        order_value, distance, customer_type, is_oversized = (100000, 10, "VIP", True)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 70000.0)

    def test_03(self):
        with self.assertRaises(ValueError):
            calculate_shipping_fee(100000, 10, "KHAC", False)

    def test_02(self):
        with self.assertRaises(ValueError):
            calculate_shipping_fee(100000, 25, "VIP", False)

    def test_01(self):
        with self.assertRaises(ValueError):
            calculate_shipping_fee(-100, 10, "VIP", False)

if __name__ == '__main__':
    unittest.main(verbosity=2)