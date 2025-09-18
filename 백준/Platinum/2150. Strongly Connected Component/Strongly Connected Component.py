import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
radj = [[] for _ in range(n + 1)]
for _ in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)
    radj[w].append(v)
visited = [False] * (n + 1)
order = []

for i in range(1, n + 1):
    if not visited[i]:
        stack = [(i, 0)]
        visited[i] = True
        while stack:
            v, idx = stack[-1]
            if idx < len(adj[v]):
                stack[-1] = (v, idx + 1)
                u = adj[v][idx]
                if not visited[u]:
                    visited[u] = True
                    stack.append((u, 0))
            else:
                stack.pop()
                order.append(v)
visited2 = [False] * (n + 1)
scc_count = 0
scc = [[] for _ in range(n)]
i = 0
for v in reversed(order):
    if not visited2[v]:
        scc_count += 1
        stack = [v]
        visited2[v] = True
        while stack:
            x = stack.pop()
            scc[i].append(x)
            for y in radj[x]:
                if not visited2[y]:
                    visited2[y] = True
                    stack.append(y)
    scc[i].sort()
    i += 1
print(scc_count)
scc.sort()
for i in scc:
    if len(i) == 0:
        continue
    print(*i,end=' ')
    print(-1)