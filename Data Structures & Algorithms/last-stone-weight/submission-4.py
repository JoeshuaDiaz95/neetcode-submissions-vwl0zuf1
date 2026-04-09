import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x == y:
                continue
            elif x < y:
                z = y - x
                heapq.heappush(stones,-z)
        if stones:
            return -stones[0]
        else: 
            return 0


        