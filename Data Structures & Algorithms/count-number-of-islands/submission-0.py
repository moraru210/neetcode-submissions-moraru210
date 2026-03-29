class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r < 0 or c < 0 or c >= COLS or r >= ROWS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for d in directions:
                dfs(r + d[0], c + d[1])
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res
                 