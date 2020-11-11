from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def UpweightedShortestPath(self, s, dest):
        # path = []
        q = []
        q.append(s)
        distance = [-1] * (self.v)
        distance[s] = 0
        while q:
            u = q.pop(0)
            for w in self.graph[u]:
                if distance[w] == -1:
                    distance[w] = distance[u] + 1
                    # path[w] = v
                    q.append(w)
        print("Shortest path from " + str(s) + " to " + str(dest) + " is " + str(distance[dest]))


g = Graph(8)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(3, 7)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(4, 7)
g.addEdge(5, 6)
g.addEdge(6, 7)
g.UpweightedShortestPath(0, 7)
