import sys
from collections import deque
input = sys.stdin.readline

a,b,c = map(int,input().split())
box = []
q = deque()
total = 0
ripe = 0

for z in range(c):
    layer = []
    for y in range(b):
        row = list(map(int,input().split()))
        for x in range(a):
            if row[x] != -1:
                total += 1
            if row[x] == 1:
                q.append((z,y,x))
                ripe += 1
        layer.append(row)
    box.append(layer)
move = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
day = 0
while q:
    for _ in range(len(q)):
        z,y,x = q.popleft()
        for dz,dy,dx in move:
            nz,ny,nx = z+dz, y+dy, x+dx
            if 0 <= nz < c and 0 <= ny < b and 0 <= nx < a:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = 1
                    ripe += 1
                    q.append((nz,ny,nx))
    if q:
        day += 1
if ripe == total:
    print(day)
else:
    print(-1)