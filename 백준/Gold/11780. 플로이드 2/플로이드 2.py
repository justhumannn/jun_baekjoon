import sys
input = sys.stdin.readline

a = int(input())
bus = int(input())
cost = [[float('inf')] * (a+1) for _ in range(a+1)]
path = [[0] * (a+1) for _ in range(a+1)]
for _ in range(bus):
    b,d,c = map(int, input().split())
    if c < cost[b][d]:
        cost[b][d] = c
        path[b][d] = d
for k in range(1,a+1):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
                path[i][j] = path[i][k]
for i in range(1,a+1):
    for j in range(1,a+1):
        if i == j or cost[i][j] == float('inf'):
            cost[i][j] = 0
        print(cost[i][j], end=' ')
    print()
def trace(i,j):
    route = [i]
    while i != j:
        i = path[i][j]
        route.append(i)
    return route
for i in range(1,a+1):
    for j in range(1,a+1):
        if cost[i][j] == 0:
            print(0)
        else:
            route = trace(i,j)
            print(len(route), *route)