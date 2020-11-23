from collections import defaultdict

def dfs(i, visited, graph, ans):
    visited[i] = True
    node = 0
    for n in graph[i]:
        if visited[n] == False:
            next_nodes, ans = dfs(n, visited, graph, ans)
            if next_nodes % 2 == 0:
                ans += 1
            else:
                node += next_nodes
    return node+1, ans

def evenForest(t_nodes, t_edges, t_from, t_to):
    graph = defaultdict(list)
    i, j = 0, 0
    while i < len(t_from) and j < len(t_to):
        graph[t_from[i]].append(t_to[j])
        graph[t_to[j]].append(t_from[i])
        i += 1
        j += 1

    ans = 0
    visited = [False] * (t_nodes + 1)
    a, ans = dfs(1, visited, graph, ans)
    print(ans)

t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]

evenForest(10, 9, t_from, t_to)
