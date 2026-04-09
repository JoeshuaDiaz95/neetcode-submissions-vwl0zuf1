class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current, total):

            if total == target:
                res.append(current[:])
                return
            if total > target or i > len(nums):
                return
            
            for j in range(i,len(nums)):
                current.append(nums[j])
                backtrack(j,current,total + nums[j])
                current.pop()
        
        backtrack(0,[],0)
        return res