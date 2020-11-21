from collections import defaultdict

def DFS(n, visited, nodes, graph):
    if visited[n] == True:
        return 0
    nodes += 1
    visited[n] = True
    for i in graph[n]:
        if visited[i] == False:
            nodes = DFS(i, visited, nodes, graph)
    return nodes

def roadsAndLibraries(n, c_lib, c_road, cities):
    graph = defaultdict(list)
    visited = [False] * (n+1)
    for i, j in cities:
        graph[i].append(j)
        graph[j].append(i)

    cost = 0
    for i in range(1, n+1):
        if visited[i] == False:
            nodes = 0
            nodes = DFS(i, visited, nodes, graph)
            cost = cost + c_lib
            if c_lib > c_road:
                cost = cost + (c_road * (nodes - 1))
            else:
                cost = cost + (c_lib * (nodes - 1))
    print(cost)


cities = [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]
roadsAndLibraries(6, 2, 5, cities)
