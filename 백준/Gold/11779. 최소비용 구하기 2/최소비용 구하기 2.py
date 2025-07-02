import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
k,e = map(int,input().split())
d = [float('inf')] * (n+1)
sequence = [(0, k)]
way = [0] * (n+1)
d[k] = 0
while sequence:
    weight, node = heapq.heappop(sequence)
    if d[node] < weight:
        continue
    for v, w in graph[node]:
        if d[v] > weight + w:
            d[v] = weight + w
            way[v] = node
            heapq.heappush(sequence, (d[v], v))
print(d[e])
way2 = []
while e != 0:
    way2.append(e)
    e = way[e]
way2.reverse()
print(len(way2))
print(*way2)