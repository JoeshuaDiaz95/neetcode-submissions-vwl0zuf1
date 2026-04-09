class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxp =0
        # for i in range(0,len(prices)-1):
        #     for n in range(i+1,len(prices)):
        #         if prices[n] - prices[i] > maxp:
        #             maxp = prices[n] - prices[i]
        # return maxp
        

        maxp=0
        l = 0

        for r in range(1,len(prices)):
            maxp = max(maxp,(prices[r] - prices[l]))
            if prices[r] < prices[l]:
                l = r
        return maxp
            