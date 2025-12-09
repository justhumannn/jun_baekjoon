import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
radj = [[] for _ in range(n)]
for _ in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)
    radj[w].append(v)

visited = [False] * n
order = []

for i in range(n):
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

scc_id = [-1] * n
scc_cnt = 0
    
for v in reversed(order):
    if scc_id[v] == -1:
        stack = [v]
        scc_id[v] = scc_cnt
        while stack:
            x = stack.pop()
            for y in radj[x]:
                if scc_id[y] == -1:
                    scc_id[y] = scc_cnt
                    stack.append(y)
        scc_cnt += 1

scc_indegree = [0] * scc_cnt

for i in range(n):
    for j in adj[i]:
        if scc_id[i] != scc_id[j]:
            scc_indegree[scc_id[j]] += 1
ans = 0
for i in range(scc_cnt):
    if scc_indegree[i] == 0:
        ans += 1
print(ans)