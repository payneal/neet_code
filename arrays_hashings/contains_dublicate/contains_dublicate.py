class ContainsDublicate():

    def __init__(self):
        pass

    # brute force
    # time complexity = O(n^2)
    # space complexity = O(1) 
    def method_1(self, nums):
        
        # for loop through numbs
        for count, value in enumerate(nums):
            # for loop again to check all nums
            for x in range (len(nums)):
                # skip index comparing but check if similar numbers
                if count != x and value == nums[x]: 
                    # we have a dublicate
                    return True
        # no duplicates
        return False
    # -----------------------------------------------------------------

    # sorting
    # time complexity =  n(log n)
    # space complexity =  O(1)
    def method_2(self, nums):
        
        # sort everything
        nums.sort()
        #  loop through all options
        for idx, value in enumerate(nums):
            # if checked all list no dups
            if idx == len(nums) -1: return False
            # found duplicates
            elif value == nums[idx+1]: return True

    # -----------------------------------------------------------------

    # hash set
    # time complexity = O(n)
    # space complexity =  O(n)
    def method_3(self, nums):
    
        # created holder
        hash_nums = set()
        # loop through all 
        for x in nums:
            # check if in set
            if x in hash_nums:
                # duplicate
                return True
            # not in set so add
            else: 
                hash_nums.add(x) 
        return False


    # set shortcut
    # time complexity = O(1) 
    # space complexity = O(n) 
    def method_4(self, nums):
        
        # create set with nums ( sets cant have duplicates) 
        numSet = set(nums)
        if len(nums) == len(numSet): return False
        return True
        
