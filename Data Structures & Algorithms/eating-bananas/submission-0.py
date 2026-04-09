import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        res = right

        def hoursperk(k: int) -> int:
            hours = 0
            for pile in piles: 
                hours += math.ceil(pile/k)
            return hours
        while left <= right:

            mid = (left + right) // 2
            if hoursperk(mid) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        