import heapq
import sys
def dikstra(start, end):
    d = [float('inf')] * (n + 1)
    sequence = [(0, start)]
    d[start] = 0
    while sequence:
        weight, node = heapq.heappop(sequence)
        if d[node] < weight:
            continue
        for v, w in graph[node]:
            if d[v] > weight + w:
                d[v] = weight + w
                heapq.heappush(sequence, (d[v], v))
    return d[end]
input = sys.stdin.readline
n,m,k = map(int, input().split())
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
time = [0] * (n+1)
for i in graph:
    time[i] = dikstra(i,k)
    time[i] += dikstra(k,i)
print(max(time))