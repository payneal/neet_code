import unittest
from binary_search import BinarySearch

class TestValidAnagram(unittest.TestCase):

    def setUp(self):
        self.bs = BinarySearch()

    def tearDown(self):
        self.bs = None

    def test_ex_1_m2(self):
        assert self.bs.m1([-1,0,3,5,9,12], 9) == 4
   
    def test_ex_2_m2(self):
        assert self.bs.m1([-1,0,3,5,9,12], 2) == -1
    


if __name__ == '__main__':
    unittest.main()
