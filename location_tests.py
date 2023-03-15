import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("LA", -86.2, 102.6)
        loc3 = Location("x", 0, 0)
        self.assertEqual(repr(loc1), "Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2), "Location('LA', -86.2, 102.6)")
        self.assertEqual(repr(loc3), "Location('x', 0, 0)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc2_ = Location("SLO", 35.3, -120.8)
        loc3 = loc2
        loc4 = Location("LA", -86.2, 102.6)
        self.assertEqual(loc1 == loc2, True)
        self.assertEqual(loc2 == loc3, True)
        self.assertEqual(loc4 == loc2, False)
        self.assertEqual(loc2_ == loc2, False)

    def test_init(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("LA", -86.2, 102.6)
        loc3 = Location("SF", 52.8, -44.4)
        loc4 = Location("ATL", -106.3, 11.9)
        loc5 = Location("NYC", -46.2, -1.77)


if __name__ == "__main__":
    unittest.main()
