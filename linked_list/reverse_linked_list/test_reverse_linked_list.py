import unittest
from reverse_linked_list import ReverseLinkedList

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



five  = ListNode( 5, None)
four = ListNode( 4, five)
three = ListNode( 3, four)
two = ListNode(2, three)
one = ListNode(1,  two)


class TestValidAnagram(unittest.TestCase):

    def setUp(self):
        self.rll =  ReverseLinkedList()

    def tearDown(self):
        self.rll = None

    def test_ex_1_m1(self):
        
        five  = ListNode( 5, None)
        four = ListNode( 4, five)
        three = ListNode( 3, four)
        two = ListNode(2, three)
        one = ListNode(1,  two)

        new_head = self.rll.m1(one)
        
        assert one.next  == None
        assert new_head.val == 5
  

    def test_ex_2_m1(self):
        
        two = ListNode(2, None)
        one = ListNode(1,  two)

        new_head = self.rll.m1(one)
        
        assert one.next  == None
        assert new_head.val == 2


    def test_ex_3_m1(self):
        
        new_head = self.rll.m1(None)
        assert new_head == None
 

    def test_ex_1_m2(self):
        
        five  = ListNode( 5, None)
        four = ListNode( 4, five)
        three = ListNode( 3, four)
        two = ListNode(2, three)
        one = ListNode(1,  two)

        new_head = self.rll.m2(one)
        
        assert one.next  == None
        assert new_head.val == 5
  

    def test_ex_2_m2(self):
        
        two = ListNode(2, None)
        one = ListNode(1,  two)

        new_head = self.rll.m2(one)
        
        assert one.next  == None
        assert new_head.val == 2



if __name__ == '__main__':
    unittest.main()
