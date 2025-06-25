a = int(input())
bus = int(input())
cost = [[float('inf')] * (a+1) for _ in range(a+1)]

for _ in range(bus):
    b,d,c = map(int, input().split())
    cost[b][d] = min(cost[b][d], c)

for k in range(1,a+1):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if i == j:
                cost[i][j] = 0
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
for i in range(1,a+1):
    for j in range(1,a+1):
        if cost[i][j] == float('inf'):
            cost[i][j] = 0
        print(cost[i][j], end=' ')
    print()