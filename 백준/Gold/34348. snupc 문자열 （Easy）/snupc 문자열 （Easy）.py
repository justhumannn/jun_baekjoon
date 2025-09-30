import bisect

S = input().strip()
n = len(S)
dict = {'s': [], 'n': [], 'u': [], 'p': [], 'c': []}
for i, ch in enumerate(S, 1):
    dict[ch].append(i)
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    m = float('inf')
    for i in 'snupc':
        m = min(m, bisect.bisect_right(dict[i], b) - bisect.bisect_left(dict[i], a))
    lo, hi = 0, m
    while lo < hi:
        mid = (lo + hi + 1) // 2
        pos = a - 1
        ok = True
        for i in 'snupc':
            idx = bisect.bisect_left(dict[i], pos + 1)
            if idx + mid - 1 >= len(dict[i]) or dict[i][idx + mid - 1] > b:
                ok = False
                break
            pos = dict[i][idx + mid - 1]
        if ok:
            lo = mid
        else:
            hi = mid - 1
    print(lo)