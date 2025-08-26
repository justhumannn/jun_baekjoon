import heapq
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
see = list(map(int, input().split()))
graph = {i :[] for i in range(0,n)}
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
sequence = [(0,0)]
distance = [float('inf')] * (n+1)
while sequence:
    weight,node = heapq.heappop(sequence)
    if weight > distance[node]:
        continue
    if node == n:
        break
    distance[node] = weight
    for n1,w in graph[node]:
        if see[n1] == 1 and n1 != n-1:
            continue
        if distance[n1] > weight+w:
            distance[n1] = weight+w
            heapq.heappush(sequence, (distance[n1], n1))
if distance[n-1] == float('inf'):
    print(-1)
else:
    print(distance[n-1])