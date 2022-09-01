import unittest
from two_sum import TwoSum

class TestValidAnagram(unittest.TestCase):

    def setUp(self):
        self.ts = TwoSum()

    def tearDown(self):
        self.ts = None

    #def test_ex_1_m1(self):
    #    assert self.ts.m1([2,7,11,15],9) == [0,1]

    #def test_ex_2_m1(self):
    #    assert self.ts.m1( [3,2,4], 6) == [1,2]

    #def test_ex_3_m1(self):
    #    assert self.ts.m1( [3,3], 6) == [0,1]

    def test_ex_1_m2(self):
        assert self.ts.m2([2,7,11,15],9) == [0,1]
    
    def test_ex_2_m1(self):
        assert self.ts.m1( [3,2,4], 6) == [1,2]

    def test_ex_3_m1(self):
        assert self.ts.m1( [3,3], 6) == [0,1]


if __name__ == '__main__':
    unittest.main()
