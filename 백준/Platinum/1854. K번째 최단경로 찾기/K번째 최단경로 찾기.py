import sys
import heapq
input = sys.stdin.readline

a,b,c = map(int, input().split())
graph = {i:[] for i in range(1,a+1)}
for _ in range(b):
    d,e,f = map(int, input().split())
    graph[d].append((e,f))
sequence = [(0,1)]
priority = [[] for _ in range(a+1)]
heapq.heappush(priority[1],0)
while sequence:
    weight, node = heapq.heappop(sequence)
    for n,w in graph[node]:
        if len(priority[n]) < c:
            heapq.heappush(priority[n], -(weight + w))
            heapq.heappush(sequence, (weight + w, n))
        elif -priority[n][0] > weight + w:
            heapq.heappop(priority[n])
            heapq.heappush(priority[n], -(weight + w))
            heapq.heappush(sequence,(weight + w,n))
for i in range(1,a+1):
    if len(priority[i]) < c:
        print(-1)
    else:
        print(-priority[i][0])