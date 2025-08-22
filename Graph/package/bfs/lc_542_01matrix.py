from typing import List
from collections import deque

data = [
    [[0,0,0],[0,1,0],[0,0,0]],
    [[0,0,0],[0,1,0],[1,1,1]]
]
def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    queue = deque()
    dist = [[-1]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append(((i,j), 0))
                dist[i][j] = 0
    while queue:
        node, d = queue.popleft()
        row, col = node[0], node[1]
        print(row, col)
        if row > 0 and dist[row-1][col] == -1:
            dist[row-1][col] = d+1
            queue.append(((row-1, col), d+1))
        if row < m-1 and dist[row+1][col] == -1:
            dist[row+1][col] = d+1
            queue.append(((row+1, col), d+1))
        if col > 0 and dist[row][col-1] == -1:
            dist[row][col-1] = d+1
            queue.append(((row, col-1), d+1))
        if col < n-1 and dist[row][col+1] == -1:
            dist[row][col+1] = d+1
            queue.append(((row, col+1), d+1))
    return dist
d = updateMatrix(data[1])
print(d)