import unittest
from contains_dublicate import ContainsDublicate

class TestDublicate(unittest.TestCase):

    def setUp(self):
        self.cd = ContainsDublicate()
    
    def tearDown(self):
        self.cd = None

    def test_ex_1_method_1(self):
        nums = [1,2,3,1]
        assert True  == self.cd.method_1(nums)

    def test_ex_2_method_1(self):
        nums = [1,2,3,4]
        assert False  == self.cd.method_1(nums)

    def test_ex_3_method_1(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        assert True  == self.cd.method_1(nums)
    
    def test_ex_1_method_2(self):
        nums = [1,2,3,1]
        assert True  == self.cd.method_2(nums)

    def test_ex_2_method_2(self):
        nums = [1,2,3,4]
        assert False  == self.cd.method_2(nums)

    def test_ex_3_method_2(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        assert True  == self.cd.method_2(nums)

    def test_ex_1_method_3(self):
        nums = [1,2,3,1]
        assert True  == self.cd.method_3(nums)

    def test_ex_2_method_3(self):
        nums = [1,2,3,4]
        assert False  == self.cd.method_3(nums)

    def test_ex_3_method_3(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        assert True  == self.cd.method_3(nums)
  
    def test_ex_1_method_4(self):
        nums = [1,2,3,1]
        assert True  == self.cd.method_4(nums)

    def test_ex_2_method_4(self):
        nums = [1,2,3,4]
        assert False  == self.cd.method_4(nums)

    def test_ex_3_method_4(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        assert True  == self.cd.method_4(nums)
  

if __name__ == '__main__':
    unittest.main()
