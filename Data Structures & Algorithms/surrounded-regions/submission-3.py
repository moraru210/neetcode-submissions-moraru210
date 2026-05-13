class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != "O":
                return
            
            board[row][col] = "T"
            
            dfs(row, col+1)
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            return

        for r in range(ROWS):
            dfs(r,0)  
            dfs(r,COLS-1)

        for c in range(COLS):
            dfs(0,c)  
            dfs(ROWS-1,c)
                

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
