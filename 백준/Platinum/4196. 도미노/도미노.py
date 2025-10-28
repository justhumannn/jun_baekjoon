import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    sequence.append(u)

def reverse_dfs(u, label):
    visited[u] = True
    scc_id[u] = label
    for v in re_graph[u]:
        if not visited[v]:
            reverse_dfs(v, label)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    graph = {i: [] for i in range(1, a + 1)}
    re_graph = {i: [] for i in range(1, a + 1)}
    for _ in range(b):
        c, d = map(int, input().split())
        graph[c].append(d)
        re_graph[d].append(c)
    visited = [False] * (a + 1)
    sequence = []
    for i in range(1, a + 1):
        if not visited[i]:
            dfs(i)
    visited = [False] * (a + 1)
    scc_id = [0] * (a + 1)
    scc_count = 0
    for v in reversed(sequence):
        if not visited[v]:
            scc_count += 1
            reverse_dfs(v, scc_count)
    indegree = [0] * (scc_count + 1)
    for u in range(1, a + 1):
        for v in graph[u]:
            if scc_id[u] != scc_id[v]:
                indegree[scc_id[v]] += 1
    ans = sum(1 for i in range(1, scc_count + 1) if indegree[i] == 0)
    print(ans)
