class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def addEdge(self, src, dist, weight):
        self.graph.append([src, dist, weight])

    def bellman_ford(self, src):
        dist = [float("inf")] * (self.v)
        dist[src] = 0

        for _ in range(self.v - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.printDist(dist)

    def printDist(self, dist):
        print("Vertex\tDistance from source")
        for i in range(self.v):
            print("{}\t\t{}".format(i, dist[i]))


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
g.bellman_ford(0)
