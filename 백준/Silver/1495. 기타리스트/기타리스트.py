import sys

input = sys.stdin.readline
n, s, m = map(int, input().split())
v = list(map(int, input().split()))
d = [[0] * (m + 1) for _ in range(n + 1)]
d[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if d[i - 1][j] == 1:
            if j - v[i - 1] >= 0:
                d[i][j - v[i - 1]] = 1
            if j + v[i - 1] <= m:
                d[i][j + v[i - 1]] = 1

result = -1
for i in range(m, -1, -1):
    if d[n][i] == 1:
        result = i
        break

print(result)