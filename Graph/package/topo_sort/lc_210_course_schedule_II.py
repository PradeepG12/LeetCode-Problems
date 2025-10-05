from typing import List

data = [
    [4, [[1,0],[2,0],[3,1],[3,2]]]
]

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph, state = build_graph(numCourses, prerequisites)
    stack = []
    for node in graph:
        if state[node] == 0:
            if not dfs(node=node, stack=stack, state=state, graph=graph):
                return []
    stack.reverse()
    return stack

def build_graph(courses, prerequisites):
    graph = {}
    state = {}
    for i in range(courses):
        graph[i] = []
        state[i] = 0
    for a, b in prerequisites:
        graph[b].append(a)
    return graph, state

def dfs(node, state, stack, graph):
    state[node] = 1
    for nei in graph[node]:
        if state[nei] == 1:
            return False
        elif state[nei] == 0:
            if not dfs(node=nei, state=state, stack=stack, graph=graph):
                return False
    state[node] = 2
    stack.append(node)
    return True

d=findOrder(data[0][0], data[0][1])
print(d)
