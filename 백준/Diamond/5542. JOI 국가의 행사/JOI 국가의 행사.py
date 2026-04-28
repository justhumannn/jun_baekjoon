import sys
from heapq import heappush, heappop

input_data = sys.stdin.read().split()

N = int(input_data[0])
M = int(input_data[1])
K = int(input_data[2])
Q = int(input_data[3])

adj = [[] for _ in range(N + 1)]
edges = []
idx = 4
for _ in range(M):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    w = int(input_data[idx+2])
    idx += 3
    adj[u].append((v, w))
    adj[v].append((u, w))
    edges.append((u, v))

festivals = []
for _ in range(K):
    festivals.append(int(input_data[idx]))
    idx += 1

queries = []
for _ in range(Q):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    idx += 2
    queries.append((u, v))

INF = 10**15
dist = [INF] * (N + 1)
pq = []

for f in festivals:
    dist[f] = 0
    heappush(pq, (0, f))

while pq:
    d, u = heappop(pq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > d + w:
            dist[v] = d + w
            heappush(pq, (dist[v], v))

mst_edges = []
for u, v in edges:
    w = dist[u] if dist[u] < dist[v] else dist[v]
    mst_edges.append((w, u, v))

mst_edges.sort(key=lambda x: x[0], reverse=True)

parent = list(range(N + 1))

def find(i):
    root = i
    while root != parent[root]:
        root = parent[root]
    curr = i
    while curr != root:
        nxt = parent[curr]
        parent[curr] = root
        curr = nxt
    return root

tree_adj = [[] for _ in range(N + 1)]
for w, u, v in mst_edges:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_u] = root_v
        tree_adj[u].append((v, w))
        tree_adj[v].append((u, w))

LOG = 18
up = [[0] * LOG for _ in range(N + 1)]
min_w = [[INF] * LOG for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)

q = [1]
head = 0
visited[1] = True

while head < len(q):
    u = q[head]
    head += 1
    for v, w in tree_adj[u]:
        if not visited[v]:
            visited[v] = True
            depth[v] = depth[u] + 1
            up[v][0] = u
            min_w[v][0] = w
            q.append(v)

for j in range(1, LOG):
    for i in range(1, N + 1):
        up[i][j] = up[up[i][j-1]][j-1]
        min_w[i][j] = min_w[i][j-1] if min_w[i][j-1] < min_w[up[i][j-1]][j-1] else min_w[up[i][j-1]][j-1]

out = []
for u, v in queries:
    ans = dist[u] if dist[u] < dist[v] else dist[v]
    
    if depth[u] < depth[v]:
        u, v = v, u
        
    diff = depth[u] - depth[v]
    for j in range(LOG):
        if (diff >> j) & 1:
            if min_w[u][j] < ans:
                ans = min_w[u][j]
            u = up[u][j]
            
    if u != v:
        for j in range(LOG - 1, -1, -1):
            if up[u][j] != up[v][j]:
                if min_w[u][j] < ans:
                    ans = min_w[u][j]
                if min_w[v][j] < ans:
                    ans = min_w[v][j]
                u = up[u][j]
                v = up[v][j]
                
        if min_w[u][0] < ans:
            ans = min_w[u][0]
        if min_w[v][0] < ans:
            ans = min_w[v][0]
            
    out.append(str(ans))

print('\n'.join(out))