#!/usr/bin/env python3
import unittest
from max_subarray_divide_conquer import max_subarray_dc


class TestCase(unittest.TestCase):

    def test_case(self):
        for arr, expected in [
            ([-1, -3, 1, -14, 18, -15], 18),
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
        ]:
            with self.subTest(array=arr, expected=expected):
                res = max_subarray_dc(arr, 0, len(arr))
                self.assertEqual(expected, res)


if __name__ == "__main__":
    unittest.main()
