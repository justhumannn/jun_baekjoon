import sys
input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    b.append(list(map(int, input().split())))
can_go = [[0] * a for _ in range(a)]
for k in range(a):
    for i in range(a):
        for j in range(a):
            if b[i][k] and b[k][j]:
                b[i][j] = 1
for i in b:
    print(*i)