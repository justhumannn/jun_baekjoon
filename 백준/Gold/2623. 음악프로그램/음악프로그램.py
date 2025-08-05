from collections import deque
a,b = map(int,input().split())
graph = {i:[] for i in range(1,a+1)}
in_degree = [0] * (a + 1)
for _ in range(b):
    d = deque(list(map(int,input().split())))
    for i in range(1,len(d)-1):
        j = d[i]
        k = d[i+1]
        graph[j].append(k)
        in_degree[k] += 1

queue = deque()
sequence = []
for i in range(1, a + 1):
    if in_degree[i] == 0:
        queue.append(i)
while queue:
    num = queue.popleft()
    sequence.append(num)
    for i in graph[num]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
if len(sequence) != a:
    print(0)
else:
    for i in sequence:
        print(i)