from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):
        new_node = [dest, weight]
        self.graph[src].insert(0, new_node)

        # For undirected
        new_node = [src, weight]
        self.graph[dest].insert(0, new_node)

    def dijkstra(self, src):
        pq = []
        dist = [-1] * (self.v)
        dist[src] = 0
        heapq.heappush(pq, (0, src))
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > dist[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if dist[neighbor] == -1:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        self.printDist(dist)

    def printDist(self, dist):
        print("Vertex\tDistance from source")
        for i in range(self.v):
            print("{}\t\t{}".format(i, dist[i]))


graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)
