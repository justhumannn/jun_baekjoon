import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
scc_id = [0] * (n + 1)
scc_list = []
scc_count = 0
for v in reversed(order):
    if not visited2[v]:
        stack = [v]
        visited2[v] = True
        temp_list = []
        scc_count += 1
        while stack:
            x = stack.pop()
            temp_list.append(x)
            scc_id[x] = scc_count
            for y in radj[x]:
                if not visited2[y]:
                    visited2[y] = True
                    stack.append(y)
        scc_list.append(temp_list)

if scc_count == 1:
    print(n)
    print(*sorted(range(1, n + 1)))
    sys.exit(0)

indegree = [0] * (scc_count + 1)
outdegree = [0] * (scc_count + 1)
dag = [[] for _ in range(scc_count + 1)]
for v in range(1, n + 1):
    for u in adj[v]:
        if scc_id[v] != scc_id[u]:
            indegree[scc_id[u]] += 1
            outdegree[scc_id[v]] += 1
            dag[scc_id[v]].append(scc_id[u])

sources = [i for i in range(1, scc_count + 1) if indegree[i] == 0]
sinks = [i for i in range(1, scc_count + 1) if outdegree[i] == 0]
if len(sources) != 1 or len(sinks) != 1:
    print(0)
    sys.exit(0)

start = sources[0]
q = deque([start])
seen = [False] * (scc_count + 1)
seen[start] = True
cnt = 1
while q:
    cur = q.popleft()
    for nxt in dag[cur]:
        if not seen[nxt]:
            seen[nxt] = True
            cnt += 1
            q.append(nxt)

if cnt != scc_count:
    print(0)
else:
    ans = sorted(scc_list[start - 1])
    print(len(ans))
    print(*ans)