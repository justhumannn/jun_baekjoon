import heapq
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = {i :[] for i in range(1,n+1)}
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
sequence = [(0,1)]
distance = [float('inf')] * (n+1)
while sequence:
    weight,node = heapq.heappop(sequence)
    if weight > distance[node]:
        continue
    if node == n:
        break
    distance[node] = weight
    for n1,w in graph[node]:
        if distance[n1] > weight+w:
            distance[n1] = weight+w
            heapq.heappush(sequence, (distance[n1], n1))
print(distance[n])