import sys
input = sys.stdin.readline

c, b = map(int, input().split())
adj = [[] for _ in range(c + 1)]
radj = [[] for _ in range(c + 1)]
for _ in range(b):
    l = list(map(int, input().split()))
    v, m = l[0], l[1]
    for w in l[2:]:
        adj[v].append(w)
        radj[w].append(v)

visited = [False] * (c + 1)
order = []
for i in range(1, c + 1):
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

visited2 = [False] * (c + 1)
scc_id = [0] * (c + 1)
sccs = []
cur_id = 0
for v in reversed(order):
    if not visited2[v]:
        stack = [v]
        visited2[v] = True
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            scc_id[x] = cur_id
            for y in radj[x]:
                if not visited2[y]:
                    visited2[y] = True
                    stack.append(y)
        sccs.append(comp)
        cur_id += 1

indegree = [0] * cur_id
for v in range(1, c + 1):
    for u in adj[v]:
        if scc_id[v] != scc_id[u]:
            indegree[scc_id[u]] += 1

zero_indegree_scc = [i for i in range(cur_id) if indegree[i] == 0]
if len(zero_indegree_scc) != 1:
    print(0)
else:
    print(len(sccs[zero_indegree_scc[0]]))