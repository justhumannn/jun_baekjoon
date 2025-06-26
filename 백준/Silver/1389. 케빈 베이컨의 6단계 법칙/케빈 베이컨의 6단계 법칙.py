from collections import deque

a, bus = map(int, input().split())
cost = [[float('inf')] * (a+1) for _ in range(a+1)]

for _ in range(bus):
    b,d = map(int, input().split())
    cost[b][d] = 1
    cost[d][b] = 1

for k in range(1,a+1):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if i == j:
                cost[i][j] = float('inf')
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
cabin = [0] * (a+1)
for i in range(1,a+1):
    for j in range(1,a+1):
        if i == j:
            continue
        cabin[i] += cost[i][j]
cabin = deque(cabin)
cabin.popleft()
print(cabin.index(min(cabin)) + 1)