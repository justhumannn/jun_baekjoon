import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = list(map(int, input().split()))

if b <= c:
    print(sum(d) * b)
else:
    ans = 0
    for i in range(a - 2):
        if d[i + 1] > d[i + 2]:
            two = min(d[i], d[i + 1] - d[i + 2])
            d[i] -= two
            d[i + 1] -= two
            ans += two * (b + c)

            three = min(d[i], d[i + 1], d[i + 2])
            d[i] -= three
            d[i + 1] -= three
            d[i + 2] -= three
            ans += three * (b + 2 * c)
        else:
            three = min(d[i], d[i + 1], d[i + 2])
            d[i] -= three
            d[i + 1] -= three
            d[i + 2] -= three
            ans += three * (b + 2 * c)

            two = min(d[i], d[i + 1])
            d[i] -= two
            d[i + 1] -= two
            ans += two * (b + c)

        ans += d[i] * b
        d[i] = 0

    two = min(d[-2], d[-1])
    ans += two * (b + c)
    d[-2] -= two
    d[-1] -= two
    ans += (d[-2] + d[-1]) * b
    print(ans)