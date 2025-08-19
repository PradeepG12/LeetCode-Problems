from typing import List
from collections import deque

datas = [
    [[2,1,1],[1,1,0],[0,1,1]],
    [[2,1,1],[0,1,1],[1,0,1]],
    [[0,2]],
    [[1,2]],
    [[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]],
]

def orangesRotting(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    if (m or n) < 1: return -1
    mins = 0
    queue = deque()
    fresh_oranges = change_to_rotten = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append(([i,j], 0))
            elif grid[i][j] == 1:
                fresh_oranges += 1
    while queue:
        cell, time = queue.popleft()
        row, col = cell[0], cell[1]
        # if visited_grid[row][col] == [1]:
        #     continue
        # visited_grid[row][col] = [1]
        mins = max(time, mins)
        if col < n-1:
            if grid[row][col+1] == 1:
                change_to_rotten += 1
                queue.append(([row, col+1], time+1))
                grid[row][col+1] = 2
        if row < m -1:
            if grid[row+1][col] == 1:
                change_to_rotten += 1
                queue.append(([row+1, col], time+1))
                grid[row+1][col] = 2
        if col > 0:
            if grid[row][col-1] == 1:
                change_to_rotten += 1
                queue.append(([row, col-1], time+1))
                grid[row][col-1] = 2
        if row > 0:
            if grid[row-1][col] == 1:
                change_to_rotten += 1
                queue.append(([row-1, col], time+1))
                grid[row-1][col] = 2
    if fresh_oranges != change_to_rotten: return -1
    return mins

print([orangesRotting(data) for data in datas])