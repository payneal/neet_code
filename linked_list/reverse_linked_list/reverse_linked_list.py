class ReverseLinkedList:

    def __init__(self):
        pass



    # TIME = O(n)   
    # Space = O(1)
    def m1(self, head):

        prev, cur = None, head

        while cur:
            temp = cur.next # 2
            cur.next = prev # 1 -> None     
            prev = cur # move to next link 
            cur = temp # current = 2 

        return prev

    # recrusive
    # time = O(n)  
    # space = O(n) 
    def m2(self, head):
        
        if not head: return None

        newhead = head

        if head.next: 
            newhead = self.m2(head.next)
            head.next.next = head
        head.next = None 

        return newhead


