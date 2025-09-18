import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
cost = [0] + list(map(int, input().split()))  # 1-based

adj = [[] for _ in range(n+1)]
radj = [[] for _ in range(n+1)]
for i in range(1, n+1):
    line = input().strip()
    for j, c in enumerate(line, start=1):
        if c == '1':
            adj[i].append(j)
            radj[j].append(i)

visited = [False] * (n+1)
order = []
def dfs1(v):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            dfs1(u)
    order.append(v)
for i in range(1, n+1):
    if not visited[i]:
        dfs1(i)
visited = [False] * (n+1)
sccs = []

def dfs2(v, comp):
    visited[v] = True
    comp.append(v)
    for u in radj[v]:
        if not visited[u]:
            dfs2(u, comp)

for v in reversed(order):
    if not visited[v]:
        comp = []
        dfs2(v, comp)
        sccs.append(comp)
answer = 0
for comp in sccs:
    answer += min(cost[v] for v in comp)
print(answer)