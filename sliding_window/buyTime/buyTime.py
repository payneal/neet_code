class BuyTime:

    def __init__(self):
        pass
    
    # time =  O(n)
    # space = O(1)
    def m1(self, prices):
        
        high = 0
        l = 0
        
        # loop through prices
        for r in range( 1, len(prices)):
            
            # if r > l set l = r
            if prices[r] < prices[l]:
                l = r 

            # set high
            high = max(high, prices[r]-prices[l])
            

        print("here is high: {}".format(high))
        return high
