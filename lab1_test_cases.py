import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        # checking for exception
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)
        # checking for emptiness
        self.assertEqual(max_list_iter([]), None)
        # checking for max in each location
        self.assertEqual(max_list_iter([1, 1, 1, 1, 5]), 5)
        self.assertEqual(max_list_iter([1, 1, 1, 5, 1]), 5)
        self.assertEqual(max_list_iter([1, 1, 5, 1, 1]), 5)
        self.assertEqual(max_list_iter([1, 5, 1, 1, 1]), 5)
        self.assertEqual(max_list_iter([5, 1, 1, 1, 1]), 5)
        # checking for multiple max
        self.assertEqual(max_list_iter([1, 1, 1, 5, 5]), 5)
        self.assertEqual(max_list_iter([1, 1, 5, 5, 5]), 5)
        self.assertEqual(max_list_iter([1, 5, 5, 5, 5]), 5)
        self.assertEqual(max_list_iter([5, 5, 5, 5, 5]), 5)
        # checking for increasing max
        self.assertEqual(max_list_iter([1, 2, 3, 4, 5]), 5)
        # checking for non-int
        self.assertEqual(max_list_iter([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)

    def test_reverse_rec(self):
        # given test case
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        # checking for exception
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        # checking for normal 0-9 (even)
        self.assertEqual(reverse_rec([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        # checking for odd
        self.assertEqual(reverse_rec([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        # checking for other val type
        self.assertEqual(reverse_rec(["a", "b", "c"]), ["c", "b", "a"])
        # checking for empty list
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        # given test case
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        # checking for exception
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(2, 0, 5, tlist)
        # checking for empty list
        self.assertEqual(bin_search(5, 0, 10, []), None)
        # checking for every location
        self.assertEqual(bin_search(0, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)
        self.assertEqual(bin_search(1, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 1)
        self.assertEqual(bin_search(2, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)
        self.assertEqual(bin_search(3, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 3)
        self.assertEqual(bin_search(4, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 4)
        self.assertEqual(bin_search(5, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertEqual(bin_search(6, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 6)
        self.assertEqual(bin_search(7, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 7)
        self.assertEqual(bin_search(8, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
        self.assertEqual(bin_search(9, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        # checking for when target location before low
        self.assertEqual(bin_search(2, 5, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        self.assertEqual(bin_search(6, 7, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        self.assertEqual(bin_search(9, 10, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        # checking for when target location after high
        self.assertEqual(bin_search(7, 0, 5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        self.assertEqual(bin_search(8, 0, 6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        self.assertEqual(bin_search(9, 0, 7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        # checking for when target location does not exist
        self.assertEqual(bin_search(11, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        self.assertEqual(bin_search(12, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        self.assertEqual(bin_search(13, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)


if __name__ == "__main__":
    unittest.main()
