class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        


        res = []
        nums.sort()

        def backtrack(start,path):
            # not sure the stopping condition
            res.append(path[:])


            for i in range(start,len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
            
            # include
                path.append(nums[i])
                backtrack(i+1,path)
            # not include next value
                path.pop()

        backtrack(0,[])
        return res
