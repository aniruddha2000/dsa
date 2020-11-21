from collections import defaultdict

def DFS(n, visited, value, graph):
    if visited[n] == True:
        return 0
    value += 1
    visited[n] = True
    for i in graph[n]:
        if visited[i] == False:
            value = DFS(i, visited, value, graph)
    return value

def journeyToMoon(n, astronaut):
    graph = defaultdict(list)
    visited = [False] * (n)

    for a1, a2 in astronaut:
        graph[a1].append(a2)
        graph[a2].append(a1)

    prev_val = 0
    ans = 0
    value = 0
    for i in range(n):
        if visited[i] == False:
            value = DFS(i, visited, value, graph)
            ans += (prev_val * value)
            prev_val += value
            value = 0
    print(ans)



astronaut = [[0, 1], [2, 3], [0, 4]]
# astronaut = [[0, 2]]
journeyToMoon(5, astronaut)
