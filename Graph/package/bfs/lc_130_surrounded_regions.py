from typing import List
from collections import deque
datas = [
    [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
    [["X"]],
    [["X","O","X"],["X","O","X"],["X","O","X"]],
]

def solve(board: List[List[str]]) -> None:
    m = len(board)
    n = len(board[0])
    queue = deque()
    # eligible = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                if board[i][j] == "O":
                    board[i][j] = "P"
                    queue.append((i,j))
    while queue:
        row, col = queue.popleft()
        if row > 0 and board[row-1][col] == "O": #up
            board[row-1][col] = "P"
            queue.append((row-1, col))
        if row < m-1 and board[row+1][col] == "O": #down
            board[row+1][col] = "P"
            queue.append((row+1, col))
        if col > 0 and board[row][col-1] == "O": #left
            board[row][col-1] = "P"
            queue.append((row, col-1))
        if col < n-1 and board[row][col+1] == "O": #right
            board[row][col+1] = "P"
            queue.append((row, col+1))
    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "P":
                board[i][j] = "O"
    print(board)
d = solve(datas[-1])
print(d)