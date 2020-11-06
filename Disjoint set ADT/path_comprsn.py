from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.edges = defaultdict(list)

    def addEdge(self, u, v):
        self.edges[u].append(v)


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank =rank


def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent

def union(subsets, u, v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    else:
        subsets[u].parent = v
        subsets[v].rank += 1

def isCycle(graph):
    subsets = []
    for u in range(graph.v):
        subsets.append(Subset(u, 0))

    for u in graph.edges:
        for v in graph.edges[u]:
            u_set = find(subsets, u)
            v_set = find(subsets, v)
            if u_set == v_set:
                return True
            else:
                union(subsets, u_set, v_set)


g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if isCycle(g):
    print("Cycle True")
else:
    print("Cycle False")
