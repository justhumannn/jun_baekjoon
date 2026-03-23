import sys

n, m = map(int, sys.stdin.readline().split())

matrix_a = []
for _ in range(n):
    matrix_a.append(list(map(int, sys.stdin.readline().split())))

m_b, k = map(int, sys.stdin.readline().split())

matrix_b = []
for _ in range(m_b):
    matrix_b.append(list(map(int, sys.stdin.readline().split())))

matrix_c = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            matrix_c[i][j] += matrix_a[i][x] * matrix_b[x][j]

for row in matrix_c:
    print(*row)