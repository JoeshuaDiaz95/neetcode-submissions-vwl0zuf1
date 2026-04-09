from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        visited = set()
        visiting = set()
        def dfs(c):

            if c in visited:
                return True
            if c in visiting:
                return False
            visiting.add(c)
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            visited.add(c)
            return True
        



        for num in range(numCourses):
            if not dfs(num):
                return False
        return True

        