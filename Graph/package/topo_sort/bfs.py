from collections import defaultdict, deque

class BFS_TopoSort:

    def __init__(self, graph_list):
        self.graph = self.build_graph(graph_list)

    def build_graph(self, graph_list):

        graph = defaultdict(list)
        for u, v in graph_list:
            graph[v].append(u)
        return graph

    def get_indegrees(self):

        in_degrees = {}
        for u, v in self.graph.items():
            if u not in in_degrees:
                in_degrees[u] = 0
            for node in v:
                if node not in in_degrees:
                    in_degrees[node] = 0
                in_degrees[node] += 1
        return in_degrees

    def get_order(self):
        queue = deque()
        in_degrees = self.get_indegrees()
        for key, val in in_degrees.items():
            if val == 0:
                queue.append(key)
        order_list = []
        while queue:
            key = queue.popleft()
            order_list.append(key)
            for node in self.graph[key]:
                in_degrees[node] -= 1
                if in_degrees[node] == 0:
                    queue.append(node)
        return order_list


data = [
    [[1,0],[2,0],[3,1],[3,2]],
    [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
]
b = BFS_TopoSort(data[0])
print(dict(b.graph))
print(b.get_indegrees())
print(b.get_order())
