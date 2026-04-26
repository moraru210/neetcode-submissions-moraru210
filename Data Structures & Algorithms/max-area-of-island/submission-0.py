class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        maxArea = 0
        cur = 0

        def dfs(x, y):
            nonlocal maxArea, cur
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0 or (x,y) in visit:
                return 0

            visit.add((x,y))
            return 1 +dfs(x+1,y) + dfs(x,y+1) + dfs(x-1,y) + dfs(x,y-1)

        
        for i in range(ROWS):
            for j in range(COLS):
                maxArea = max(maxArea, dfs(i,j))
        return maxArea