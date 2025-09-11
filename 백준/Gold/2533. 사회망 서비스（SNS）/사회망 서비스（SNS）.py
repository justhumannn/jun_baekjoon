import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(u):
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v][0], dp[v][1])
dfs(1)
print(min(dp[1][0], dp[1][1]))