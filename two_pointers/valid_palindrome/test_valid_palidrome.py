import unittest
from valid_palidrome import ValidPalidrome

class TestValidPalidrome(unittest.TestCase):

    def setUp(self):
        self.vp = ValidPalidrome()

    def tearDown(self):
        self.vp = None

    def test_ex_1_m2(self):
        assert self.vp.m2("A man, a plan, a canal: Panama") == True

    def test_ex_2_m2(self):
        assert self.vp.m2("race a car") == False
    
    def test_ex_3_m2(self):
         assert self.vp.m1(" ") == True


if __name__ == '__main__':
    unittest.main()
