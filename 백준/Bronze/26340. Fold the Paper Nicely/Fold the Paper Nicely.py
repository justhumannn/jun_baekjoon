t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    print(f"Data set: {a} {b} {k}")
    x, y = a, b
    for _ in range(k):
        if x >= y:
            x //= 2
        else:
            y //= 2
    if x < y:
        x, y = y, x
    print(x, y)
    print()