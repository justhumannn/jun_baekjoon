import sys
from collections import deque
import copy
from itertools import combinations
input = sys.stdin.readline


def spreadvirus(templab, n, m):
    queue = deque()
    for r in range(n):
        for c in range(m):
            if templab[r][c] == 2:
                queue.append((r, c))
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and templab[nr][nc] == 0:
                templab[nr][nc] = 2
                queue.append((nr, nc))
    return templab
def countsafe(templab, n, m):
    safearea = 0
    for r in range(n):
        for c in range(m):
            if templab[r][c] == 0:
                safearea += 1
    return safearea

n, m = map(int,input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))

emptyspots = []
for r in range(n):
    for c in range(m):
        if lab[r][c] == 0:
            emptyspots.append((r, c))

maxsafearea = 0

for combo in combinations(emptyspots, 3):
    templab = copy.deepcopy(lab)
    
    for r, c in combo:
        templab[r][c] = 1
        
    infectedlab = spreadvirus(templab, n, m)
    currentsafe = countsafe(infectedlab, n, m)
    maxsafearea = max(maxsafearea, currentsafe)

print(maxsafearea)