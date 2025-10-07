from typing import List
import heapq

data = [
    [[0,2],[1,3]],
    [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
]

def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_elevation = 0
    queue = [(grid[0][0], 0, 0)] # e, i, j
    while queue:
        elevation, i, j = heapq.heappop(queue)
        max_elevation = max(max_elevation, elevation)
        visited.add((i, j))
        if i == n-1 and j == n-1:
            break
        for r, c in directions:
            i_r, j_c = r+i, c+j
            if (0 <= i_r <= n-1 and 0 <= j_c <= n-1) and (i_r, j_c) not in visited:
                heapq.heappush(queue, (grid[i_r][j_c], i_r, j_c))
    return max_elevation

data = swimInWater(data[1])
print(data)