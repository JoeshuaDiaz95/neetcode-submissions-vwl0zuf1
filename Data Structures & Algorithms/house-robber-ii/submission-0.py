class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        #case a where you rob the first house
        
        dpa = [0] * (n-1)

        dpa[0] = nums[0]
        dpa[1] = max(nums[0],nums[1])

        for i in range(2,n-1):
            dpa[i] = max(dpa[i-1], dpa[i-2]+ nums[i])
        
        #case b
        dpb = [0] * (n-1)

        dpb[0] = nums[1]
        dpb[1] = max(nums[1],nums[2])

        for l in range(2,n-1):
            dpb[l] = max(dpb[l-1], dpb[l-2] + nums[l+1])
        
        return max(dpa[-1],dpb[-1])

        