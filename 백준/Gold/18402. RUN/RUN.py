import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    dist = [float('inf')] * (len(graph) + 1)
    dist[start] = 0
    sequence = [(0, start)]
    while sequence:
        weight, node = heapq.heappop(sequence)
        if dist[node] < weight:
            continue
        for n, w in graph[node]:
            if dist[n] > weight + w:
                dist[n] = weight + w
                heapq.heappush(sequence, (dist[n], n))
    return dist

a = int(input())
b = int(input())
c = int(input())
graph = {i:[] for i in range(1,a+1)}
d = int(input())
for _ in range(d):
    e,f,g = map(int, input().split())
    graph[f].append((e, g))
result = dijkstra(b)
cont = 0
for i in range(1,a+1):
    if result[i] <= c:
        cont += 1
print(cont)