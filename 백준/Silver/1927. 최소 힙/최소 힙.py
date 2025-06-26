import heapq
import sys
input = sys.stdin.readline
a = int(input())
heap = []
for i in range(a):
    b = int(input())
    if b == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, b)