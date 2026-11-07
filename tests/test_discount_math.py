"""Regression checks for the deliberately limited fixed-cost/fee model."""
import unittest


def max_discount(price, fixed_cost, fee_rate, target_margin):
    denominator = 1 - fee_rate - target_margin
    if price <= 0 or fixed_cost < 0 or denominator <= 0:
        raise ValueError('invalid or infeasible assumptions')
    cap = 1 - fixed_cost / (price * denominator)
    if cap < 0:
        raise ValueError('target infeasible at original price')
    return cap


def margin(price, fixed_cost, fee_rate, discount):
    net = price * (1 - discount)
    return (net * (1 - fee_rate) - fixed_cost) / net


class DiscountTest(unittest.TestCase):
    def test_no_fee(self):
        cap = max_discount(100, 70, 0, .18)
        self.assertAlmostEqual(cap, .14634146341463417)
        self.assertAlmostEqual(margin(100, 70, 0, cap), .18)
        self.assertGreater(margin(100, 70, 0, .12), .18)
        self.assertLess(margin(100, 70, 0, .15), .18)

    def test_percentage_fee(self):
        cap = max_discount(100, 50, .1, .2)
        self.assertAlmostEqual(margin(100, 50, .1, cap), .2)

    def test_infeasible(self):
        with self.assertRaises(ValueError):
            max_discount(100, 90, .1, .2)
        with self.assertRaises(ValueError):
            max_discount(100, 1, .5, .5)


if __name__ == '__main__':
    unittest.main()
