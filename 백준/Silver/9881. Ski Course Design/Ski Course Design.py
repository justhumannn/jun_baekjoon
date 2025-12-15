import sys
input = sys.stdin.readline

n = int(input())
hills = [int(input()) for _ in range(n)]

ans = float('inf')

for L in range(0, 101):
    R = L + 17
    cost = 0
    for h in hills:
        if h < L:
            cost += (L - h) ** 2
        elif h > R:
            cost += (h - R) ** 2
    ans = min(ans, cost)

print(ans)