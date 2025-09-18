import sys
import heapq
from collections import deque
input = sys.stdin.readline

def dijkstra(start, n, graph, removed):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        w, u = heapq.heappop(pq)
        if dist[u] < w:
            continue
        for v, cost in graph[u]:
            if removed[u][v]:
                continue
            if dist[v] > w + cost:
                dist[v] = w + cost
                heapq.heappush(pq, (dist[v], v))
    return dist

def remove_edges(d, dist, rgraph, removed):
    q = deque([d])
    visited = [False] * len(dist)
    while q:
        cur = q.popleft()
        if visited[cur]:
            continue
        visited[cur] = True
        for prev, cost in rgraph[cur]:
            if dist[prev] + cost == dist[cur]:
                removed[prev][cur] = True
                q.append(prev)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split())

    graph = [[] for _ in range(n)]
    rgraph = [[] for _ in range(n)]
    removed = [[False]*n for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        rgraph[v].append((u, p))

    dist = dijkstra(s, n, graph, removed)
    remove_edges(d, dist, rgraph, removed)
    dist2 = dijkstra(s, n, graph, removed)

    print(dist2[d] if dist2[d] != float('inf') else -1)