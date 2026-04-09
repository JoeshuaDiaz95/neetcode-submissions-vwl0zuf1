from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for  a,b in prerequisites:
            graph[b].append(a)
        
        visiting = set()
        visited = set()
        order = []


        def dfs(course):

            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for c in graph[course]:
                if not dfs(c):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order[::-1]


        