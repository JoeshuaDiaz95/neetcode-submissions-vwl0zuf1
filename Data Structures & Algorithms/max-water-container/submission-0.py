class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        currentmax = 0

        while l < r:
            currentarea = min(height[l],height[r])*(r-l)
            currentmax = max(currentmax, currentarea)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return currentmax