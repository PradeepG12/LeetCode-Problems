class TopoSort:
    def __init__(self, graph_list=None):
        self.graph = self.build_graph(graph_list)

    def build_graph(self, graph_list):
        if not graph_list: return {}
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in graph_list:
            graph[u] = v
        return graph
