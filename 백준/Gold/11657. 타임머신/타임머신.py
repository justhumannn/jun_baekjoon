import sys
input = sys.stdin.readline
def bellman_ford(graph, node):
    distance = [float('inf')] * (node + 1)
    distance[1] = 0
    for i in range(node-1):
        for u in graph:
            for v,w in graph[u]:
                if distance[u] != float('inf') and distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
    for u in graph:
        for v, w in graph[u]:
            if distance[u] != float('inf') and distance[v] > distance[u] + w:
                print(-1)
                return
    for i in range(2,node +1):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])
node, edge = map(int, input().split())
graph = {i : [] for i in range(1,node + 1)}
for j in range(edge):
    b,c,d = map(int, input().split())
    graph[b].append((c,d))
bellman_ford(graph, node)