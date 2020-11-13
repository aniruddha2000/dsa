from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xset = self.find(parent, x)
        yset = self.find(parent, y)

        if xset == yset:
            return

        if rank[xset] < rank[yset]:
            parent[xset] = yset
        elif rank[yset] < rank[xset]:
            parent[yset] = xset
        else:
            parent[xset] = yset
            rank[yset] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        while e < self.v -1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        self.printArr(result)

    def printArr(self, result):
        minCost = 0
        print("Edges in the constructed MST")
        for u, v, w in result:
            minCost += w
            print("{} -- {} == {}".format(u, v, w))
        print("Minimum Spanning Tree" , minCost)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

# Function call
g.kruskal()
