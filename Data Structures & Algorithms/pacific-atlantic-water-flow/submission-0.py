class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visited, prev_height):
            if( r < 0 or c < 0 or
                r >= ROWS or c >= COLS
                or prev_height > heights[r][c]
                or (r,c) in visited
            ):
                return
            visited.add((r,c))

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r + dr, c + dc,visited, heights[r][c])

        


        #pacific
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])

        #atl
        for r in range(ROWS):
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        for c in range(COLS):
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        return list(pac & atl)
