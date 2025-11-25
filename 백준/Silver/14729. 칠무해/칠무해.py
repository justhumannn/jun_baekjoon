import sys
import heapq

input = sys.stdin.readline

N = int(input())
max_heap = []

for _ in range(N):
    score = float(input())
    if len(max_heap) < 7:
        heapq.heappush(max_heap, -score)
    else:
        if score < -max_heap[0]:
            heapq.heapreplace(max_heap, -score)

result = sorted([-x for x in max_heap])

for x in result:
    print(f"{x:.3f}")