import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start):
    if len(graph) == 0:
        return -1
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

a,b = map(int, input().split())
graph = {i:[] for i in range(1, a + 1)}
for _ in range(b):
    c,d,e = map(int, input().split())
    graph[c].append((d, e))
    graph[d].append((c, e))
c = int(input())
doner = []
for _ in range(c):
    d = int(input())
    doner.append(d)
distance = dijkstra(graph, 1)
min_distance = float('inf')
for i in doner:
    if distance[i] < min_distance:
        min_distance = distance[i]
        min_num = i
print(min_num, min_distance)