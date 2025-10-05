from collections import defaultdict

class DFS_TopoSort:

    def __init__(self, graph_list):
        self.state_tracker = {}
        self.graph = self.build_graph(graph_list)

    def build_graph(self, graph_list):
        graph = defaultdict(list)
        for u, v in graph_list:
            if u not in self.state_tracker:
                self.state_tracker[u] = 0
            if v not in self.state_tracker:
                self.state_tracker[v] = 0
            graph[v].append(u)
        return graph

    def get_order(self):
        stack = []
        for node in list(self.graph):
            if self.state_tracker[node] == 0:
                self.dfs(node, stack)
        stack.reverse()
        return stack

    def dfs(self, node, stack):
        self.state_tracker[node] = 1
        for neighbor in self.graph[node]:
            if self.state_tracker[neighbor] == 0:
                self.dfs(node=neighbor, stack=stack)
        if self.state_tracker[node] == 1:
            self.state_tracker[node] = 2
            stack.append(node)
        return

data = [
    [[1,0],[2,0],[3,1],[3,2]],
    [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
]
b = DFS_TopoSort(data[0])
print(dict(b.graph))
print(b.state_tracker)
print(b.get_order())