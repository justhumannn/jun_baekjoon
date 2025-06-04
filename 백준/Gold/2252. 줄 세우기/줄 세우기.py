from collections import deque
node_num, edge_num = map(int, input().split())
graph = {i: [] for i in range(1,node_num+1)}
in_degree = [0] * (node_num + 1)
for i in range(edge_num):
    a,b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
queue = deque()
sequence = []
for i in range(1, node_num + 1):
    if in_degree[i] == 0:
        queue.append(i)
while queue:
    num = queue.popleft()
    sequence.append(num)
    for i in graph[num]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
print(*sequence)