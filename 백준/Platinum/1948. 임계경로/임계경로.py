import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
rev_adj = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    rev_adj[v].append((u, w))
    indegree[v] += 1
start, end = map(int, input().split())
time_val = [0] * (n + 1)
q = deque([start])
while q:
    u = q.popleft()
    for v, w in adj[u]:
        if time_val[u] + w > time_val[v]:
            time_val[v] = time_val[u] + w
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

visited = [False] * (n + 1)
visited[end] = True
rq = deque([end])
edge_count = 0
while rq:
    v = rq.popleft()
    for u, w in rev_adj[v]:
        if time_val[u] + w == time_val[v]:
            edge_count += 1
            if not visited[u]:
                visited[u] = True
                rq.append(u)
print(time_val[end])
print(edge_count)