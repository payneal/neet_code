import unittest
from valid_parentheses import ValidParentheses

class TestValidAnagram(unittest.TestCase):

    def setUp(self):
        self.vp = ValidParentheses()

    def tearDown(self):
        self.vp = None

    def test_ex_1_m2(self):
        assert self.vp.m1("()") == True
    
    def test_ex_2_m1(self):
        assert self.vp.m1("()[]{}") == True

    # def test_ex_3_m1(self):
    #     assert self.vp.m1("(]") == False 


if __name__ == '__main__':
    unittest.main()
