from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i]!= -1:
            return self.find(parent,parent[i])

    def union(self, parent, u, v):
        uset = self.find(parent, u)
        vset = self.find(parent, v)
        parent[uset] = vset

    def isCycle(self):
        parent = [-1] * self.v
        for i in self.graph:
            for j in self.graph[i]:
                u = self.find(parent, i)
                v = self.find(parent, j)
                if u == v:
                    return True
                self.union(parent, u, v)


g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCycle():
    print("Cycle True")
else:
    print("Cycle False")
