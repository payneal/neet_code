class TwoSum:

    def __init__(self):
        pass

    # time = O(n^2)
    # space = O(1) 
    def m1(self, nums, target):
        
        # loop through nums get index
        for idx,value in enumerate(nums):
            # loop through nums not including index
            for x in range(len(nums)):
                if x != idx:
                    # if any == target then done 
                    if target == value + nums[x]:
                        return [ idx, x] 
   
    
    # time = O(n)
    # space = O(n)
    def m2(self, nums, target):
       
        # create hash map
        hashMap = {}

        # loop through nums get idx,value
        for idx, num in enumerate( nums):
            # value - target check if in hash map 
            value = target - num

            # if value in hash map you have answer
            if value in hashMap:
                return [hashMap[value], idx]
            else:
                # keep building hashMap
                hashMap[num] = idx

