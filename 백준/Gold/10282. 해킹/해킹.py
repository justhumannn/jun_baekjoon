import heapq
import sys
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    n,d,c = map(int,input().split())
    graph = {i:[] for i in range(1,n+1)}
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    distance = [float('inf')] * (n+1)
    distance[c] = 0
    sequence = [(0,c)]
    while sequence:
        weight,node = heapq.heappop(sequence)
        if distance[node] < weight:
            continue
        for n1,w in graph[node]:
            if distance[n1] > weight + w:
                distance[n1] = weight + w
                heapq.heappush(sequence,(distance[n1],n1))
    max_computer = 0
    max_time = 0
    for i in distance:
        if i != float('inf'):
            if i > max_time:
                max_time = i
            max_computer += 1
    print(max_computer, max_time)