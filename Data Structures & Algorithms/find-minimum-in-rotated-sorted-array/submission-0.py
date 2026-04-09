class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1  # Minimum is to the right of mid
            else:
                r = mid      # Minimum is at mid or to the left

        return nums[l]