import sys
input = sys.stdin.readline
a,bus = map(int, input().split())
INF = int(1e9)
cost = [[INF] * (a+1) for _ in range(a+1)]
for _ in range(bus):
    b,d,c = map(int, input().split())
    cost[b][d] = c
for k in range(1,a+1):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
min_road = INF
for i in range(1,a+1):
    if cost[i][i] < min_road:
        min_road = cost[i][i]
print(-1 if min_road == INF else min_road)