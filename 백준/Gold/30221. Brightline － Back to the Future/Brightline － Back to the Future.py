import sys
from collections import deque
input = sys.stdin.readline

def spfa():
    distance = [float('inf')] * (node + 1)
    in_queue = [False] * (node + 1)
    distance[1] = 0
    q = deque([1])
    in_queue[1] = True

    while q:
        u = q.popleft()
        in_queue[u] = False
        for v, w in graph[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                if not in_queue[v]:
                    q.append(v)
                    in_queue[v] = True
    for i in range(2, node + 1):
        if distance[i] < 0:
            print(i)

node, edge = map(int, input().split())
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    b, c, d, e = input().split()
    b, c, e = int(b), int(c), int(e)
    if d == 'b':
        graph[b].append((c, e))
    else:
        graph[b].append((c, -e))

spfa()