s, d = map(int, input().split())
if (s + d) % 2 != 0 or (s - d) % 2 != 0:
    print(-1)
else:
    a = (s + d) // 2
    b = (s - d) // 2
    if a < 0 or b < 0:
        print(-1)
    else:
        print(max(a, b), min(a, b))