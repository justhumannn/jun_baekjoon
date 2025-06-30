from collections import deque
import sys
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    node_num, edge_num = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = {i: [] for i in range(1,node_num+1)}
    in_degree = [0] * (node_num + 1)
    for i in range(edge_num):
        a,b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    queue = deque()
    target = int(input())
    complete_time = [0] * (node_num + 1)
    for i in range(1, node_num + 1):
        if in_degree[i] == 0:
            queue.append(i)
            complete_time[i] = time[i]
    while queue:
        num = queue.popleft()
        for i in graph[num]:
            complete_time[i] = max(complete_time[i], complete_time[num] + time[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
    print(complete_time[target])