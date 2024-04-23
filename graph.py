class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight=1):
        self.adj[node1].append((node2, weight))

    def add_edge_both(self, node1, node2, weight=1):
        self.adj[node1].append((node2, weight))
        self.adj[node2].append((node1, weight))

    def print_path(self, s, v):
        if v == s:
            print(s.key)
        elif v.parent is None:
            print("No path found")
        else:
            self.print_path(s, v.parent)
            print(f"->{v.key}")


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.color = "white"
        self.distance = None
        self.f = 0
