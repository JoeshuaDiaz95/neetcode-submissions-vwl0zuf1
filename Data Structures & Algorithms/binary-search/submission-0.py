class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursearch(left: int, right: int) -> int:
            if left > right:
                return - 1
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                return recursearch(left, midpoint-1)
            else:
                return recursearch(midpoint+1, right)

        return(recursearch(0, len(nums)-1))