import sys
input = sys.stdin.readline

n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
ans = []
if n <= 4:
    r = 1
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if j not in graph[i]:
                ans.append((i, j))
else:
    r = 2
    for i in range(2, n + 1):
        if i not in graph[1]:
            ans.append((1, i))
print(len(ans))
print(r)
for u, v in ans:
    print(u, v)