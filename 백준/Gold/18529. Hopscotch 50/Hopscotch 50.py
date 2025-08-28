import sys
input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
positions = [[] for _ in range(k + 1)]
for i in range(n):
    for j in range(n):
        positions[grid[i][j]].append((i, j))
for num in range(1, k + 1):
    if not positions[num]:
        print(-1)
        sys.exit(0)
dp = [[10**9] * len(positions[i]) for i in range(k + 1)]
for i in range(len(positions[1])):
    dp[1][i] = 0
for num in range(2, k + 1):
    for j, (x2, y2) in enumerate(positions[num]):
        for p, (x1, y1) in enumerate(positions[num - 1]):
            dp[num][j] = min(dp[num][j], dp[num - 1][p] + abs(x1 - x2) + abs(y1 - y2))
answer = min(dp[k])
print(answer if answer < 10**9 else -1)