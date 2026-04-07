import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [input().strip() for _ in range(rows)]
L = [[0] * (cols + 2) for _ in range(rows + 2)]
R = [[0] * (cols + 2) for _ in range(rows + 2)]
for i in range(rows - 1, -1, -1):
    for j in range(cols):
        if grid[i][j] == '1':
            L[i][j] = L[i+1][j-1] + 1
            R[i][j] = R[i+1][j+1] + 1
ans = 0
for i in range(rows):
    for j in range(cols):
        limit = L[i][j] if L[i][j] < R[i][j] else R[i][j]
        for k in range(limit, ans, -1):
            if R[i+k-1][j-k+1] >= k and L[i+k-1][j+k-1] >= k:
                ans = k
                break
print(ans)