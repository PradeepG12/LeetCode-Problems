from typing import List
from collections import deque

def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    colored_set = {i: -1 for i in range(n)}
    
    for node in range(n):
        if colored_set[node] == -1:
            colored_set[node] = 1
            queue = deque([node])
            while queue:
                node_idx = queue.popleft()
                for edge in graph[node_idx]:
                    if colored_set[edge] == -1:
                        colored_set[edge] = 1 if colored_set[node_idx] == 0 else 0
                        queue.append(edge)
                    elif colored_set[edge] == colored_set[node_idx]:
                        return False
    return True
