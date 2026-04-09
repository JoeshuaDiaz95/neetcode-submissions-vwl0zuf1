class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i: int) -> None:

            if i == len(nums):
                res.append(path[:])
                return
            
            #select value
            path.append(nums[i])
            backtrack(i+1)

            #not select value
            path.pop()

            backtrack(i + 1)

        backtrack(0)

        return res