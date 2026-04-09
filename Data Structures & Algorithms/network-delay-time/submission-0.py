from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v,w))
        

        min_heap = [(0,k)]
        max_time = 0
        visited = set()


        while min_heap:

            time, node = heapq.heappop(min_heap)

            if node in visited: 
                continue
            
            max_time = time
            visited.add(node)

            for neighbor, weight in edges[node]:
                if neighbor  not in visited:
                    heapq.heappush(min_heap,(time + weight, neighbor))
        
        return max_time if len(visited) == n else -1

# remember how to add values to default dict
# remember how to use a heapq initilizing it, adding values and popping values




        