import unittest

from ambit.range import Range


class TestRange(unittest.TestCase):

    def test_interval(self):
        r1 = Range(1, 3)
        self.assertEqual(r1.interval, 2)

    def test_positive_range_is_true(self):
        r1 = Range(0, 1)
        self.assertTrue(r1)

    def test_negative_range_is_true(self):
        r1 = Range(0, -1)
        self.assertTrue(r1)

    def test_zero_range_is_false(self):
        r1 = Range(0, 0)
        self.assertFalse(r1)

    def test_null_range_is_false(self):
        r1 = Range(None, None)
        self.assertFalse(r1)

    def test_addition(self):
        r1 = Range(1, 3)
        r2 = Range(2, 5)
        self.assertEqual(r1 + r2, 5)
        self.assertEqual(r2 + r1, 5)

    def test_subtraction(self):
        r1 = Range(0, 4)
        r2 = Range(0, 2)
        self.assertEqual(r1 - r2, 2)
        self.assertEqual(r2 - r1, -2)

    def test_multiplication(self):
        r1 = Range(0, 3)
        r2 = Range(0, 2)
        self.assertEqual(r1 * r2, 6)
        self.assertEqual(r2 * r1, 6)

    def test_union(self):
        r1 = Range(2, 6)
        r2 = Range(3, 8)
        self.assertEqual(r1 | r2, Range(2, 8))

    def test_union_float(self):
        r1 = Range(1.2, 1.5)
        r2 = Range(1.3, 1.7)
        self.assertEqual(r1 | r2, Range(1.2, 1.7))

    def test_union_mixed_int_float(self):
        r1 = Range(1.2, 4)
        r2 = Range(1.8, 3)
        self.assertEqual(r1 | r2, Range(1.2, 4))

    def test_intersection(self):
        r1 = Range(2, 6)
        r2 = Range(4, 8)
        self.assertEqual(r1 & r2, Range(4, 6))

    def test_intersection_float(self):
        r1 = Range(1.2, 1.6)
        r2 = Range(1.4, 1.8)
        self.assertEqual(r1 & r2, Range(1.4, 1.6))

    def test_intersection_mixed_float(self):
        r1 = Range(1.2, 6)
        r2 = Range(3, 6.4)
        self.assertEqual(r1 & r2, Range(3, 6))
