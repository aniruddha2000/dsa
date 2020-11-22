def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xset = find(parent, x)
    yset = find(parent, y)

    if xset == yset:
        return

    if rank[xset] < rank[yset]:
        parent[xset] = yset
    elif rank[yset] < rank[xset]:
        parent[yset] = xset
    else:
        parent[xset] = yset
        rank[yset] += 1


def kruskals(g_nodes, g_from, g_to, g_weight):
    graph = []
    i, j, k = 0, 0, 0
    while i < len(g_from) and j < len(g_to) and k < len(g_weight):
        graph.append([g_from[i], g_to[j], g_weight[k]])
        i += 1
        j += 1
        k += 1

    graph = sorted(graph, key=lambda item: item[2])
    i, e = 0, 0
    parent = []
    rank = []
    for node in range(g_nodes+1):
        parent.append(node)
        rank.append(0)

    result = []
    while e < g_nodes - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    minCost = 0
    for u, v, w in result:
        minCost += w

    print(minCost)


g_from = [1, 1, 1, 1, 2, 3, 4]
g_to = [2, 3, 4, 5, 3, 4, 5]
g_weight = [20, 50, 70, 90, 30, 40, 60]

kruskals(5, g_from, g_to, g_weight)
