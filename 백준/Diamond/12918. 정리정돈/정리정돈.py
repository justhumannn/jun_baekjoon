import sys
import math

input_data = sys.stdin.read().split()
N = int(input_data[0])
idx = 1

U = []
V = []

for _ in range(N):
    x = int(input_data[idx])
    y = int(input_data[idx+1])
    idx += 2
    
    if x < 0:
        U.append((x, y))
    elif x > 0:
        V.append((x, y))
        
a = len(U)
b = len(V)

M = a + b

if M == 0:
    print("0.000")
    sys.exit()

INF = 1e15
cost = [[INF] * M for _ in range(M)]

for i in range(a):
    for j in range(b):
        dx = U[i][0] + V[j][0]
        dy = U[i][1] - V[j][1]
        cost[i][j] = math.sqrt(dx * dx + dy * dy)
        
for i in range(a):
    cost[i][b + i] = float(abs(U[i][0]))
    
for i in range(b):
    cost[a + i][i] = float(abs(V[i][0]))
    
for i in range(b):
    for j in range(a):
        cost[a + i][b + j] = 0.0
        
u = [0.0] * (M + 1)
v = [0.0] * (M + 1)
p = [0] * (M + 1)
way = [0] * (M + 1)

for i in range(1, M + 1):
    p[0] = i
    j0 = 0
    minv = [INF] * (M + 1)
    used = [False] * (M + 1)
    
    while True:
        used[j0] = True
        i0 = p[j0]
        delta = INF
        j1 = 0
        
        for j in range(1, M + 1):
            if not used[j]:
                cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
                    
        for j in range(M + 1):
            if used[j]:
                u[p[j]] += delta
                v[j] -= delta
            else:
                minv[j] -= delta
                
        j0 = j1
        if p[j0] == 0:
            break
            
    while True:
        j1 = way[j0]
        p[j0] = p[j1]
        j0 = j1
        if j0 == 0:
            break
            
ans = -v[0]
print(f"{ans:.3f}")