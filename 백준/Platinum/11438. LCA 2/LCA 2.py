import sys

tokens = sys.stdin.read().split()
n = int(tokens[0])
adj = [[] for _ in range(n + 1)]
idx = 1
for _ in range(n - 1):
    u = int(tokens[idx])
    v = int(tokens[idx + 1])
    idx += 2
    adj[u].append(v)
    adj[v].append(u)

depth = [-1] * (n + 1)
parent = [[0] * (n + 1) for _ in range(18)]
stack = [1]
depth[1] = 0
while stack:
    curr = stack.pop()
    d = depth[curr] + 1
    for nxt in adj[curr]:
        if depth[nxt] == -1:
            depth[nxt] = d
            parent[0][nxt] = curr
            stack.append(nxt)
for j in range(1, 18):
    prev = parent[j - 1]
    curr = parent[j]
    for i in range(1, n + 1):
        curr[i] = prev[prev[i]]
m = int(tokens[idx])
idx += 1
out = []
for _ in range(m):
    u = int(tokens[idx])
    v = int(tokens[idx + 1])
    idx += 2
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for j in range(18):
        if diff & (1 << j):
            u = parent[j][u]
    if u == v:
        out.append(str(u))
    else:
        for j in range(17, -1, -1):
            if parent[j][u] != parent[j][v]:
                u = parent[j][u]
                v = parent[j][v]
        out.append(str(parent[0][u]))
sys.stdout.write('\n'.join(out) + '\n')