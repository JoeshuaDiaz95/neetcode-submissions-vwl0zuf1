from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        component = 0

        if n == 0: 
            return component


        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)

        

        for i in range(n):
            if i not in visited:
                dfs(i)
                component += 1
        
        return component



        