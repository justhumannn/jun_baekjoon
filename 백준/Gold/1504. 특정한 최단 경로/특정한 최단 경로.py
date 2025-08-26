import heapq
import sys
input = sys.stdin.readline
def dijkstra(graph, start):
    distance = [float('inf')] * (len(graph)+1)
    distance[start] = 0
    sequence = [(0,start)]
    while sequence:
        weight, node = heapq.heappop(sequence)
        if weight > distance[node]:
            continue
        for n,w in graph[node]:
            if distance[n] > weight+ w:
                distance[n] = weight+ w
                heapq.heappush(sequence, (weight+w, n))
    return distance

a,b = map(int, input().split())
graph = {i:[] for i in range(1,a+1)}
for _ in range(b):
    n1,n2,w1 = map(int, input().split())
    graph[n1].append((n2,w1))
    graph[n2].append((n1,w1))
v1,v2 = map(int, input().split())
d1 = dijkstra(graph, 1)
dv1 = dijkstra(graph, v1)
dv2 = dijkstra(graph, v2)
path1 = d1[v1] + dv1[v2] + dv2[a]
path2 = d1[v2] + dv2[v1] + dv1[a]
ans = min(path1, path2)
print(ans if ans < float('inf') else -1)