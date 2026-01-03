import math

m = int(input())
for _ in range(m):
    n, s = map(int, input().split())
    times = list(map(int, input().split()))
    slowest = max(times)
    required = s * slowest
    print(math.ceil(required / 1000))