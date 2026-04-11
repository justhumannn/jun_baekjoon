import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
depth = [-1] * (n + 1)
dist = [0] * (n + 1)
parent = [[0] * 17 for _ in range(n + 1)]
q = deque([1])
depth[1] = 0
while q:
    curr = q.popleft()
    for nxt, weight in graph[curr]:
        if depth[nxt] == -1:
            depth[nxt] = depth[curr] + 1
            dist[nxt] = dist[curr] + weight
            parent[nxt][0] = curr
            q.append(nxt)
for j in range(1, 17):
    for i in range(1, n + 1):
        if parent[i][j - 1] != 0:
            parent[i][j] = parent[parent[i][j - 1]][j - 1]
m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    orig_u = u
    orig_v = v
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for j in range(17):
        if diff & (1 << j):
            u = parent[u][j]
    if u == v:
        lca = u
    else:
        for j in range(16, -1, -1):
            if parent[u][j] != 0 and parent[u][j] != parent[v][j]:
                u = parent[u][j]
                v = parent[v][j]
        lca = parent[u][0]
    print(dist[orig_u] + dist[orig_v] - 2 * dist[lca])