import heapq
n, m = map(int, input().split())
limit = max(n, m) * 2 + 1
graph = {i: [(1, i + 1), (0, i * 2), (1, i - 1)] for i in range(limit)}
d = [float('inf')] * limit
sequence = [(0, n)]
d[n] = 0
while sequence:
    weight, node = heapq.heappop(sequence)
    if d[node] < weight:
        continue
    for w, v in graph[node]:
        if 0 <= v < limit and d[v] > weight + w:
            d[v] = weight + w
            heapq.heappush(sequence, (d[v], v))
print(d[m])