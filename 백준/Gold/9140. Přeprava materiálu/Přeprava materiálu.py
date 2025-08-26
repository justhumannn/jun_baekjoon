import sys
import heapq
input = sys.stdin.readline
while True:
    n, m, start, end = map(int, input().split())
    if n == 0 and m == 0 and start == 0 and end == 0:
        break
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    sequence = [(0, start)]
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    while sequence:
        weight, node = heapq.heappop(sequence)
        if weight > distance[node]:
            continue
        for n1, w in graph[node]:
            if distance[n1] > weight + w:
                distance[n1] = weight + w
                heapq.heappush(sequence, (distance[n1], n1))
    print(distance[end])