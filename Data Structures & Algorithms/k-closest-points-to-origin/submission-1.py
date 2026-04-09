import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            d = (x)**2 + (y)**2
            val = (-d,x,y)
            heapq.heappush(heap,val)
            if len(heap) > k:
                heapq.heappop(heap)
        for (_,x,y) in heap:
            result.append([x,y])
        return result

            
