import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def sum_digits(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s

n = int(input())
adj = [[] for _ in range(n)]
radj = [[] for _ in range(n)]
for i in range(n):
    nxt = (i + sum_digits(i + 1)) % n
    adj[i].append(nxt)
    radj[nxt].append(i)

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

visited2 = [False] * n
comp = [-1] * n
sccs = []
for v in reversed(order):
    if not visited2[v]:
        stack = [v]
        visited2[v] = True
        comp[v] = len(sccs)
        members = [v]
        while stack:
            x = stack.pop()
            for y in radj[x]:
                if not visited2[y]:
                    visited2[y] = True
                    comp[y] = len(sccs)
                    stack.append(y)
                    members.append(y)
        sccs.append(members)

scc_cycle_size = [0] * len(sccs)
for cid, members in enumerate(sccs):
    if len(members) > 1:
        scc_cycle_size[cid] = len(members)
    else:
        v = members[0]
        if adj[v][0] == v:
            scc_cycle_size[cid] = 1

dp = [(-1, -1)] * n

def solve(v):
    if dp[v][0] != -1:
        return dp[v]
    c = comp[v]
    if scc_cycle_size[c] > 0:
        dp[v] = (0, scc_cycle_size[c])
        return dp[v]
    nxt = adj[v][0]
    d, cyc = solve(nxt)
    dp[v] = (d + 1, cyc)
    return dp[v]

ans = 0
for i in range(n):
    d, cyc = solve(i)
    ans = max(ans, d + cyc)
print(ans)