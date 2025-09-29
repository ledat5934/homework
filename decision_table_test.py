# test_all_cases.py

import unittest
from dynamic_shipping import calculate_shipping_fee

class TestAllProvidedCases(unittest.TestCase):

    def test_case_01(self):
        fee = calculate_shipping_fee(300000, 0.1, "THUONG", True)
        self.assertAlmostEqual(fee, 70000)

    def test_case_02(self):
        fee = calculate_shipping_fee(300000, 0.5, "MOI", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_03(self):
        fee = calculate_shipping_fee(200000, 0.5, "THUONG", False)
        self.assertAlmostEqual(fee, 20000)

    def test_case_04(self):
        fee = calculate_shipping_fee(400000, 0.5, "THUONG", False)
        self.assertAlmostEqual(fee, 20000)

    def test_case_05(self):
        fee = calculate_shipping_fee(700000, 0.5, "THUONG", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_06(self):
        fee = calculate_shipping_fee(200000, 0.5, "VIP", False)
        self.assertAlmostEqual(fee, 14000)

    def test_case_07(self):
        fee = calculate_shipping_fee(400000, 0.5, "VIP", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_08(self):
        fee = calculate_shipping_fee(600000, 0.5, "VIP", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_09(self):
        fee = calculate_shipping_fee(300000, 7, "MOI", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_10(self):
        fee = calculate_shipping_fee(200000, 7, "THUONG", False)
        self.assertAlmostEqual(fee, 30000)

    def test_case_11(self):
        fee = calculate_shipping_fee(400000, 7, "THUONG", False)
        self.assertAlmostEqual(fee, 30000)

    def test_case_12(self):
        fee = calculate_shipping_fee(500000, 7, "THUONG", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_13(self):
        fee = calculate_shipping_fee(200000, 7, "VIP", False)
        self.assertAlmostEqual(fee, 21000)

    def test_case_14(self):
        fee = calculate_shipping_fee(400000, 7, "VIP", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_15(self):
        fee = calculate_shipping_fee(600000, 7, "VIP", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_16(self):
        fee = calculate_shipping_fee(300000, 17, "MOI", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_17(self):
        fee = calculate_shipping_fee(200000, 17, "THUONG", False)
        self.assertAlmostEqual(fee, 40500)

    def test_case_18(self):
        fee = calculate_shipping_fee(400000, 17, "THUONG", False)
        self.assertAlmostEqual(fee, 40500)

    def test_case_19(self):
        fee = calculate_shipping_fee(500000, 17, "THUONG", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_20(self):
        fee = calculate_shipping_fee(200000, 17, "VIP", False)
        self.assertAlmostEqual(fee, 28350)

    def test_case_21(self):
        fee = calculate_shipping_fee(400000, 17, "VIP", False)
        self.assertAlmostEqual(fee, 0)

    def test_case_22(self):
        fee = calculate_shipping_fee(600000, 17, "VIP", False)
        self.assertAlmostEqual(fee, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)