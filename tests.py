import unittest
from funcs import *


class MyTestCase(unittest.TestCase):
    # # test brute force method
    def test_brute_force(self):
        self.assertEqual(brute_force("AATCGAG", "CCATCGG"), (5, "ATCGG"))
        self.assertEqual(brute_force("ABC", "C"), (1, "C"))

    # test lcs method
    def test_lcs(self):
        self.assertEqual(lcs_method('AATCGAG', 'CCATCGG', 7, 7), (5, 'ATCGG'))
        self.assertEqual(lcs_method('ABC', 'CD', 3, 2), (1, 'C'))



if __name__ == "__main__":
    unittest.main()
