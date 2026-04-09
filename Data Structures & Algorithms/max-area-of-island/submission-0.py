class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        maxarea = 0

        def dfs(r,c):

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r,c) in visited or 
                grid[r][c] == 0
            ):
                return 0

            visited.add((r,c))
            area = 1

            area += dfs(r-1,c)
            area += dfs(r+1,c)
            area += dfs(r,c-1)
            area += dfs(r,c+1)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxarea = max(maxarea, dfs(r,c))
        return maxarea