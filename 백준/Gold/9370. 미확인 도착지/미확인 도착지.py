import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    sequence = [(0, start)]
    
    while sequence:
        cost, node = heapq.heappop(sequence)
        if distance[node] < cost:
            continue
            
        for n, w in graph[node]:
            if distance[n] > cost + w:
                distance[n] = cost + w
                heapq.heappush(sequence, (cost + w, n))
    
    return distance
a = int(input())
for _ in range(a):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    gh = 0
    for _ in range(m):
        b, c, d = map(int, input().split())
        graph[b].append((c, d))
        graph[c].append((b, d))
        if (b == g and c == h) or (c == g and b == h):
            gh = d
    arrive = []
    for _ in range(t):
        b = int(input())
        arrive.append(b)
    s_distance = dijkstra(graph, s, n)
    g_distance = dijkstra(graph, g, n)
    h_distance = dijkstra(graph, h, n)
    result = []
    for i in arrive:
        path1 = s_distance[g] + gh + h_distance[i]
        path2 = s_distance[h] + gh + g_distance[i]
        min_path = min(path1, path2)
        if s_distance[i] == min_path and s_distance[i] != float('inf'):
            result.append(i)
    result.sort()
    print(*result)