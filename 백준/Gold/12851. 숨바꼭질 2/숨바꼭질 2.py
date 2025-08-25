import heapq
n, m = map(int, input().split())
limit = max(n, m) * 2 + 1
d = [float('inf')] * limit
count = [0] * limit
sequence = [(0, n)]
d[n] = 0
count[n] = 1
while sequence:
    weight, node = heapq.heappop(sequence)
    if d[node] < weight:
        continue
    for v in (node - 1, node + 1, node * 2):
        if 0 <= v < limit:
            if d[v] > weight + 1:
                d[v] = weight + 1
                count[v] = count[node]
                heapq.heappush(sequence, (d[v], v))
            elif d[v] == weight + 1:
                count[v] += count[node]
print(d[m])
print(count[m])