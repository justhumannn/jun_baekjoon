import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
k,l = map(int,input().split())
d = [float('inf')] * (n+1)
sequence = [(0, k)]
d[k] = 0
while sequence:
    weight, node = heapq.heappop(sequence)
    if d[node] < weight:
        continue
    for v, w in graph[node]:
        if d[v] > weight + w:
            d[v] = weight + w
            heapq.heappush(sequence, (d[v], v))
print(d[l])