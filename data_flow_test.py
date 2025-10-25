import unittest
from dynamic_shipping import calculate_shipping_fee 

class TestShippingFee(unittest.TestCase):

    def test_01_invalid_order_value(self):
        order_value, distance, customer_type, is_oversized = (-100, 10, "VIP", False)
        with self.assertRaises(ValueError):
            calculate_shipping_fee(order_value, distance, customer_type, is_oversized)

    def test_02_invalid_distance(self):
        order_value, distance, customer_type, is_oversized = (100000, 25, "VIP", False)
        with self.assertRaises(ValueError):
            calculate_shipping_fee(order_value, distance, customer_type, is_oversized)

    def test_03_vip_free_ship(self):
        order_value, distance, customer_type, is_oversized = (350000, 4, "VIP", False)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 0)

    def test_04_vip_paid_shipping(self):
        order_value, distance, customer_type, is_oversized = (100000, 15, "VIP", False)
        self.assertAlmostEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 26250.0)

    def test_05_thuong_free_ship(self):
        order_value, distance, customer_type, is_oversized = (600000, 8, "THUONG", False)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 0)
    def test_06_thuong_paid_shipping(self):
        order_value, distance, customer_type, is_oversized = (100000, 4, "THUONG", False)
        self.assertAlmostEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 20000.0)
    def test_07_vip_oversized(self):
        order_value, distance, customer_type, is_oversized = (100000, 10, "VIP", True)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 70000.0)

    def test_08_invalid_customer_type(self):
        order_value, distance, customer_type, is_oversized = (100000, 10, "KHAC", False)
        with self.assertRaises(ValueError):
            calculate_shipping_fee(order_value, distance, customer_type, is_oversized)
    def test_09_moi_customer(self):
        order_value, distance, customer_type, is_oversized = (100000, 10, "MOI", False)
        self.assertEqual(calculate_shipping_fee(order_value, distance, customer_type, is_oversized), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
