import sys
import heapq

input = sys.stdin.readline

n = int(input())
locations = []
for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        locations.append((o, h))
    else:
        locations.append((h, o))

d = int(input())
locations.sort(key=lambda x: x[1])

pq = []
ans = 0
for start, end in locations:
    if end - start > d:
        continue
    heapq.heappush(pq, start)
    limit = end - d
    while pq and pq[0] < limit:
        heapq.heappop(pq)
    ans = max(ans, len(pq))
print(ans)