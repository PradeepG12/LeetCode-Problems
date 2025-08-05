from typing import List
from collections import defaultdict, deque

data = [
    [[1,1,0],[1,1,0],[0,0,1]],
    [[1,0,0],[0,1,0],[0,0,1]],
]

def findCircleNumBrute(isConnected: List[List[int]]) -> int:
    # build graph
    graph = defaultdict(list)
    n = len(isConnected)
    m = len(isConnected[0])
    for i in range(n):
        graph[i] = []
        for j in range(m):
            if i == j:
                continue
            if isConnected[i][j] == 1:
                graph[i].append(j)
    print(graph)

    def get_dfs_output():
        # helper
        def dfs(node):
            visited.add(node)
            for new_node in graph[node]:
                if new_node not in visited:
                    dfs(new_node)
        # calculate
        count = 0
        visited = set()
        for node in graph:
            if node not in visited:
                dfs(node)
                count += 1
        return count
    def get_bfs_output():
        # calculate
        count = 0
        visited = set()
        queue = deque()
        for node in graph:
            if node not in visited:
                queue.append(node)
                while queue:
                    current_node = queue.popleft()
                    if current_node not in visited:
                        visited.add(current_node)
                    for new_node in graph[current_node]:
                        if new_node not in visited:
                            queue.append(new_node)
                count += 1
        return count
    return get_bfs_output()


def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()
    count = 0
    def dfs(node):
        queue = deque([node])
        while queue:
            current_node = queue.popleft()
            for i in range(n):
                if isConnected[current_node][i] == 1 and i not in visited:
                    visited.add(i)
                    queue.append(i)
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            count += 1
    return count

