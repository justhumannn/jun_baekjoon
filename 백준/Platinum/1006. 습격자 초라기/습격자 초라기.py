import sys
input = sys.stdin.readline

def recur(start, a, b, c):
    for i in range(start, n):
        a[i + 1] = min(b[i] + 1, c[i] + 1)
        if n1[i] + n2[i] <= w: a[i + 1] = min(a[i + 1], a[i] + 1)
        if i > 0 and n1[i - 1] + n1[i] <= w and n2[i - 1] + n2[i] <= w: a[i + 1] = min(a[i + 1],a[i - 1] + 2)

        if i < n - 1:
            b[i + 1] = a[i + 1] + 1
            if n1[i + 1] + n1[i] <= w: b[i + 1] = min(b[i + 1], c[i] + 1)

            c[i + 1] = a[i + 1] + 1
            if n2[i + 1] + n2[i] <= w: c[i + 1] = min(c[i + 1], b[i] + 1)

    return a, b, c

t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))

    a = [0 for _ in range(n + 1)]
    b = [0 for _ in range(n + 1)]
    c = [0 for _ in range(n + 1)]
    a[0] = 0
    b[0] = 1
    c[0] = 1
    a, b, c = recur(0, a, b, c)
    ans = a[n]

    if n > 1 and n1[0] + n1[n - 1] <= w:
        a[1] = 1
        b[1] = 2
        if n2[0] + n2[1] <= w:
            c[1] = 1
        else:
            c[1] = 2

        a, b, c = recur(1, a, b, c)
        ans = min(ans, c[n - 1] + 1)

    if n > 1 and n2[0] + n2[n - 1] <= w:
        a[1] = 1
        c[1] = 2
        if n1[0] + n1[1] <= w:
            b[1] = 1
        else:
            b[1] = 2

        a, b, c = recur(1, a, b, c)
        ans = min(ans, b[n - 1] + 1)
    if n > 1 and n1[0] + n1[n - 1] <= w and n2[0] + n2[n - 1] <= w:
        a[1] = 0
        b[1] = 1
        c[1] = 1

        a, b, c = recur(1, a, b, c)
        ans = min(ans, a[n - 1] + 2)
    print(ans)