class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub = -float('inf')

        currsum = -float('inf')

        for num in nums:
            currsum = max(num, currsum+num)
            maxSub = max(currsum,maxSub)
        
        return maxSub


        