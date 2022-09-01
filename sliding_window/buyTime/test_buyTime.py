import unittest
from buyTime import BuyTime

class TestValidAnagram(unittest.TestCase):

    def setUp(self):
        self.bt = BuyTime()

    def tearDown(self):
        self.bt = None

    def test_ex_1_m1(self):
        assert self.bt.m1([[7,1,5,3,6,4]]) == 5

    # def test_ex_2_m1(self):
    #     assert self.bt.m1([7,6,4,3,1]) == 0

if __name__ == '__main__':
    unittest.main()
