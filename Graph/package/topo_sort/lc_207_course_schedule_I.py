from typing import List
from collections import defaultdict, deque


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    
    def build_graph():
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for u, v in prerequisites:
            graph[v].append(u)
        return graph

    def get_indegrees(graph):
        in_degrees = defaultdict(int)
        for node, edges in graph:
            if node not in in_degrees:
                in_degrees[node] = 0
            for nei in edges:
                if nei not in in_degrees:
                    in_degrees[nei] = 0
                in_degrees[nei] += 1
        return in_degrees

    graph = build_graph()
    in_degrees = get_indegrees(graph)
    queue = deque()
    for key, val in in_degrees.items():
        if val == 0:
            queue.append(key)
    ol = []
    while queue:
        node = queue.popleft()
        ol.append(node)
        for nei in graph[node]:
            in_degrees[nei] -= 1
            if in_degrees[nei] == 0:
                queue.append(nei)
    return len(ol) == len(graph)