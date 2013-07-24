import unittest

from ambit.interval import Interval


class TestInterval(unittest.TestCase):

    def test_interval(self):
        r1 = Interval(1, 3)
        self.assertEqual(r1.size, 3)

    def test_positive_range_is_true(self):
        r1 = Interval(0, 1)
        self.assertTrue(r1)

    def test_negative_range_is_true(self):
        r1 = Interval(0, -1)
        self.assertTrue(r1)

    def test_zero_range_is_false(self):
        r1 = Interval(0, 0)
        self.assertFalse(r1)

    def test_null_range_is_false(self):
        r1 = Interval(None, None)
        self.assertFalse(r1)

    def test_addition(self):
        r1 = Interval(1, 3)
        r2 = Interval(2, 5)
        self.assertEqual(r1 + r2, Interval(3, 8))
        self.assertEqual(r2 + r1, Interval(3, 8))

    def test_subtraction(self):
        r1 = Interval(0, 4)
        r2 = Interval(0, 2)
        self.assertEqual(r1 - r2, Interval(-2, 4))
        self.assertEqual(r2 - r1, Interval(-4, 2))

    def test_multiplication(self):
        r1 = Interval(2, 4)
        r2 = Interval(1, 6)
        self.assertEqual(r1 * r2, Interval(2, 24))
        self.assertEqual(r2 * r1, Interval(2, 24))

    def test_division(self):
        r1 = Interval(2, 6)
        r2 = Interval(4, 8)
        self.assertEqual(r1 / r2, Interval(0, 1))

    def test_floor_division(self):
        r1 = Interval(3, 8)
        r2 = Interval(2.3, 4)
        self.assertEqual(r1 // r2, Interval(0, 3.0))

    def test_zero_division(self):
        r1 = Interval(2, 4)
        r2 = Interval(0, 3)
        with self.assertRaises(ZeroDivisionError):
            r1 / r2

    def test_iadd(self):
        r = Interval(0, 3)
        with self.assertRaises(ValueError):
            r += 1

    def test_isub(self):
        r = Interval(0, 3)
        with self.assertRaises(ValueError):
            r -= 1

    def test_imul(self):
        r = Interval(0, 3)
        with self.assertRaises(ValueError):
            r *= 1

    def test_idiv(self):
        r = Interval(0, 3)
        with self.assertRaises(ValueError):
            r /= 1

    def test_union(self):
        r1 = Interval(2, 6)
        r2 = Interval(3, 8)
        self.assertEqual(r1 | r2, Interval(2, 8))

    def test_union_float(self):
        r1 = Interval(1.2, 1.5)
        r2 = Interval(1.3, 1.7)
        self.assertEqual(r1 | r2, Interval(1.2, 1.7))

    def test_union_mixed_int_float(self):
        r1 = Interval(1.2, 4)
        r2 = Interval(1.8, 3)
        self.assertEqual(r1 | r2, Interval(1.2, 4))

    def test_intersection(self):
        r1 = Interval(2, 6)
        r2 = Interval(4, 8)
        self.assertEqual(r1 & r2, Interval(4, 6))

    def test_intersection_float(self):
        r1 = Interval(1.2, 1.6)
        r2 = Interval(1.4, 1.8)
        self.assertEqual(r1 & r2, Interval(1.4, 1.6))

    def test_intersection_mixed_float(self):
        r1 = Interval(1.2, 6)
        r2 = Interval(3, 6.4)
        self.assertEqual(r1 & r2, Interval(3, 6))

    def test_len(self):
        r = Interval(0, 3)
        self.assertEqual(len(r), 4)
