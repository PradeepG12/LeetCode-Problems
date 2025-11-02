from typing import List

def countUnguarded(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    grid = [[0]*n for _ in range(m)]
    # -1 = walls, 1 = guards, 1 = visited, 0 = unvisited
    def dfs(i, j, di, dj):
        if (0 > i or i > m-1) or (0 > j or j > n-1):
            return
        if grid[i][j] == -1:
            return
        grid[i][j] = 1
        dfs((i+di), (j+dj), di, dj)
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    for i, j in walls:
        grid[i][j] = -1
    for i, j in guards:
        grid[i][j] = 1
    for i, j in guards:
        for di, dj in directions:
            dfs(i+di, j+dj, di, dj)
    unoccupied_cells = 0
    for row in grid:
        unoccupied_cells += row.count(0)
    return unoccupied_cells

d = countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]])
print(d)