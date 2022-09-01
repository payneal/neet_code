class BinarySearch:
    def __init__(self):
        pass


    # time = O(log n)
    # space = O(1)
    def m1(self,nums, target):
        
        # get r and l
        l = 0
        r = len(nums) -1

        while l <= r:
            half = (l + r) // 2
            
            if nums[half] < target:
                l = half+1 
            elif nums[half] > target:
                r = half -1
            elif nums[half] == target:
                return half

        return -1
