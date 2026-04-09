class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtracking(current):
            if len(current) == len(nums):
                res.append(current[:])
                return
            
            for i in range(len(nums)):

                if used[i]:
                    continue
                
                current.append(nums[i])
                used[i] = True


                backtracking(current)
                current.pop()
                used[i] = False
        

        backtracking([])
        return res

