import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        visited = set()

        min_heap = [(0,0)]

        totalcost = 0



        while len(visited) < n:
            cost , i = heapq.heappop(min_heap)

            if i in visited:
                continue
            
            totalcost += cost
            visited.add(i)


            for j in range(n):
                if j in visited:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(min_heap, (dist, j))
        return totalcost


        