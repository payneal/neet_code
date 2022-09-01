import unittest
from valid_anagram import ValidAnagram

class TestValidAnagram(unittest.TestCase):

    def setUp(self):
        self.va = ValidAnagram()

    def tearDown(self):
        self.va = None

    def test_ex_1_m1(self):
        assert self.va.method_1("anagram", "nagaram") == True

    def test_ex_2_m1(self):  
        assert self.va.method_1("rat", "car") == False

    def test_ex_1_m2(self):
        assert self.va.method_2("anagram", "nagaram") == True

    def test_ex_2_m2(self):  
        assert self.va.method_2("rat", "car") == False

if __name__ == '__main__':
    unittest.main()
