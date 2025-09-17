import sys, math
input = sys.stdin.readline

A, B, C = map(int, input().split())
A = float(A); B = float(B); C = float(C)

low = max(0.0, (C - B) / A)
high = (C + B) / A

def f(x):
    return A * x + B * math.sin(x) - C
for _ in range(200):
    mid = (low + high) / 2.0
    if f(mid) <= 0:
        low = mid
    else:
        high = mid
ans = (low + high) / 2.0
print("{:.18f}".format(ans))