import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
w = [a[i + 1] - a[i] for i in range(n - 1)]
lo, hi = 0, 10**9
while lo < hi:
    mid = (lo + hi) // 2
    dp0s = dp0c = 0
    dp1s = -10**30
    dp1c = 0
    for x in w:
        ns0, nc0 = dp0s, dp0c
        if dp1s > ns0 or (dp1s == ns0 and dp1c > nc0):
            ns0, nc0 = dp1s, dp1c
        cand_s = dp0s + mid - x
        cand_c = dp0c + 1
        ns1, nc1 = cand_s, cand_c
        dp0s, dp0c = ns0, nc0
        dp1s, dp1c = ns1, nc1
    bests, bestc = dp0s, dp0c
    if dp1s > bests or (dp1s == bests and dp1c > bestc):
        bests, bestc = dp1s, dp1c
    if bestc >= k:
        hi = mid
    else:
        lo = mid + 1
lam = lo
dp0s = dp0c = 0
dp1s = -10**30
dp1c = 0
for x in w:
    ns0, nc0 = dp0s, dp0c
    if dp1s > ns0 or (dp1s == ns0 and dp1c > nc0):
        ns0, nc0 = dp1s, dp1c
    cand_s = dp0s + lam - x
    cand_c = dp0c + 1
    ns1, nc1 = cand_s, cand_c
    dp0s, dp0c = ns0, nc0
    dp1s, dp1c = ns1, nc1
bests, bestc = dp0s, dp0c
if dp1s > bests or (dp1s == bests and dp1c > bestc):
    bests, bestc = dp1s, dp1c
print(lam * k - bests)