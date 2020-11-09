class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def add_edges(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Only for undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.v):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edges(0, 1)
    graph.add_edges(0, 4)
    graph.add_edges(1, 2)
    graph.add_edges(1, 3)
    graph.add_edges(1, 4)
    graph.add_edges(2, 3)
    graph.add_edges(3, 4)
    graph.print_graph()
