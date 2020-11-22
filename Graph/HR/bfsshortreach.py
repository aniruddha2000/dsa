from collections import defaultdict


def bfs(n, m, edges, s):
    graph = defaultdict(list)
    distance = [-1] * (n+1)

    for e1, e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)

    q = []
    q.append(s)
    distance[s] = 0
    while q:
        head = q.pop(0)
        for i in graph[head]:
            if distance[i] == -1:
                distance[i] = 1 + distance[head]
                q.append(i)

    result = []
    for i in distance[1:]:
        if i > 0:
            result.append(str(i*6))
        if i < 0:
            result.append(str(-1))

    ans = ' '.join(result)
    print(ans)


edges = [[1, 2], [1, 3], [3, 4]]
bfs(5, 3, edges, 1)
