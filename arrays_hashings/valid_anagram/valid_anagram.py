class ValidAnagram():

    def __init__(self):
        pass
        
    # time = O(n) 
    # space = O(n)
    def method_1(self, s, t):
    
        # check to see if lengths equal if not cant be anagram
        if len(s) != len(t): return False
        
        # create holding space for hash map
        s_map, t_map = {}, {}
        
        # loop through s + t to create map
        for x in range(len(s)):
            s_map[s[x]] = 1 + s_map.get(s[x], 0 )
            t_map[t[x]] = 1 + t_map.get(t[x], 0 )
    
        # loop through s + t map to check counts
        for x in s:
            if s_map.get(x, 0) != t_map.get(x,0): return False

        return True

    # time = O( n log n) - "think of sorting algos"
    # space =  O (1) 
    def method_2(self, s, t): 
        
        # check to see if lengths equal if not cant be anagram
        if len(s) != len(t): return False
     
        # sort both words
        t = sorted(t)
        s = sorted(s)

        # loop through words 
        for x in range(len(s)):
            if s[x] != t[x]: return False

        # valid anagram
        return True

