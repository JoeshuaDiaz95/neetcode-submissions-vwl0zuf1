class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra   # <-- merge here
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]