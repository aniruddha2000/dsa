class Graph:
    def __init__(self, numvertex):
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist = [0]*numvertex

    def set_vertex(self, vtx, id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edges(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        # For only one directed graph
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjMatrix[i][j] != -1:
                    edges.append(self.adjMatrix[i][j])
        return edges

    def get_matrix(self):
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                print(self.adjMatrix[i][j], end=" ")
            print()


g = Graph(6)
g.set_vertex(0, 'a')
g.set_vertex(1,'b')
g.set_vertex(2,'c')
g.set_vertex(3,'d')
g.set_vertex(4,'e')
g.set_vertex(5,'f')
g.set_edges('a','e',10)
g.set_edges('a','c',20)
g.set_edges('c','b',30)
g.set_edges('b','e',40)
g.set_edges('e','d',50)
g.set_edges('f','e',60)
print("Vertices of Graph")
print(g.get_vertex())
print("Edges of Graph")
print(g.get_edges())
print("Adjacency Matrix of Graph")
# print(g.get_matrix())
g.get_matrix()
