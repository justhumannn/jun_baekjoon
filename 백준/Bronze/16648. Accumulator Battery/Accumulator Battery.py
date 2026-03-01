t, p = map(int, input().split())
if p >= 20:
    x = t / (100 - p)
    ans = (p - 20) * x + 40 * x
else:
    x = t / (120 - 2 * p)
    ans = 2 * p * x
print(ans)