from collections import deque
from typing import List

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    not_visited = -1
    visited = 0
    can_flow = 1
    """

    array = [(-1,0), (1, 0), (0, -1), (0, 1)]
    m, n = len(heights), len(heights[0])

    pacific_flows = [[-1]*n for _ in range(m)]
    atlantic_flows = [[-1]*n for _ in range(m)]
    pacific_queue = deque()
    atlantic_queue = deque()

    atlantic_result, pacific_result = set(), set()
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                pacific_flows[i][j] = 1
                pacific_queue.append([i, j])
                pacific_result.add((i, j))
            if j == n-1 or i == m-1:
                atlantic_flows[i][j] = 1
                atlantic_queue.append([i, j])
                atlantic_result.add((i, j))

    while pacific_queue:
        i, j = pacific_queue.popleft()
        current_val = heights[i][j]
        for row, col in array:
            t_r, t_c = i+row, j+col
            if not (0 <= t_r < m and 0 <= t_c < n):
                continue
            if pacific_flows[t_r][t_c] == -1:
                if heights[t_r][t_c] >= current_val:
                    pacific_flows[t_r][t_c] = 1
                    pacific_queue.append([t_r, t_c])
                    pacific_result.add((t_r, t_c))

    while atlantic_queue:
        i, j = atlantic_queue.popleft()
        current_val = heights[i][j]
        for row, col in array:
            t_r, t_c = i+row, j+col
            if not (0 <= t_r < m and 0 <= t_c < n):
                continue
            if atlantic_flows[t_r][t_c] == -1:
                if heights[t_r][t_c] >= current_val:
                    atlantic_flows[t_r][t_c] = 1
                    atlantic_queue.append([t_r, t_c])
                    atlantic_result.add((t_r, t_c))
    return sorted([[i, j] for (i, j) in pacific_result & atlantic_result])

data = [
    [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
    [[1]]
]
print(pacificAtlantic(data[0]))