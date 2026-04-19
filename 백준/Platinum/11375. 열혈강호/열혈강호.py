import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    if data[0] > 0:
        adj[i] = data[1:]
match = [0] * (m + 1)
def dfs(curr, visited):
    for nxt in adj[curr]:
        if visited[nxt]: continue
        visited[nxt] = True
        if match[nxt] == 0 or dfs(match[nxt], visited):
            match[nxt] = curr
            return True
    return False
ans = 0
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    if dfs(i, visited): ans += 1
sys.stdout.write(str(ans) + '\n')