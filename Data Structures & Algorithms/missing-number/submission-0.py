class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        totaln = 0
        totalc = 0

        for i in range(len(nums)):
            totaln += nums[i]
            totalc += i
        
        totalc += len(nums)

        return totalc - totaln

        