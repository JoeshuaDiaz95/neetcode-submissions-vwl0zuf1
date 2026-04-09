class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsn = [-n for n in nums]
        heapq.heapify(numsn)
        if k > 1:
            for i in range(k-1):
                heapq.heappop(numsn)
        return -1 * heapq.heappop(numsn)


        