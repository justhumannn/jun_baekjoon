def bellman_ford(graph, edge):
    distance = [float('inf')] * (edge + 1)
    distance[0] = 0
    for i in range(edge):
        for u in graph:
            for v,w in graph[u]:
                if distance[v] > distance[u] + w and distance[u] != float('inf'):
                    distance[v] = distance[u] + w
    for u in graph:
        for v, w in graph[u]:
            if distance[v] > distance[u] + w and distance[u] != float('inf'):
                return 'YES'
    return 'NO'
a = int(input())
for i in range(a):
    node, edge, minus_edge = map(int, input().split())
    graph = {i : [] for i in range(node + 1)}
    for j in range(edge):
        b,c,d = map(int, input().split())
        graph[b].append((c,d))
        graph[c].append((b,d))
    for j in range(minus_edge):
        b,c,d = map(int, input().split())
        graph[b].append((c,-d))
    for i in range(1, node + 1):
        graph[0].append((i, 0))
    print(bellman_ford(graph, node))