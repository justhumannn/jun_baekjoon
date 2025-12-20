import math
import sys

p, a, b, c, d, n = map(int, sys.stdin.readline().split())
max_price = -1e30
max_decline = 0.0
for k in range(1, n + 1):
    price = p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)
    if price > max_price:
        max_price = price
    else:
        diff = max_price - price
        if diff > max_decline:
            max_decline = diff
print(f"{max_decline:.10f}")