class ValidPalidrome:
    def __init__(self):
        pass
    
    # time = O(n) 
    # space =  O(1) 
    def m1(self, string):
        
        # convert all uppercase to lower
        string = string.lower()
        
        # remove all non alpha
        string = "".join(filter(str.isalnum, string))
        
        # for loop  half
        for idx  in range(int(len(string)/2)):
            # if first sec and 2nd sec !  equal then fail 
            if string[idx] != string[len(string)-1-idx]: return False

        return True    
    
    # time = O(n) 
    # space =  O(1) 
    def m2(self, string):

        # creat pointers for end and last
        l, r = 0, len(string)-1

        # while loop r < l
        while l < r:

            # while loop get l pointer  
            while l < r and string[l].isalnum() == False:
                l += 1 

            # while loop get r pointer
            while l < r and string[r].isalnum() == False:
                r -=1
        
            # print("compare  l={} vs r={}".format(string[l], string[-(1+r)]))
        
            # if not equal return false
            if string[l].lower() != string[r].lower(): return False

            l += 1
            r -= 1 

        return True
    



