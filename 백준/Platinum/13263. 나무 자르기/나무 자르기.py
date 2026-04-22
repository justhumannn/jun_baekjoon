import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0] * n
hull = [0] * n
sz = 1
ptr = 0
for i in range(1, n):
    x = a[i]
    while ptr + 1 < sz:
        idx1 = hull[ptr]
        idx2 = hull[ptr + 1]
        if dp[idx2] - dp[idx1] <= x * (b[idx1] - b[idx2]):
            ptr += 1
        else:
            break
    best_j = hull[ptr]
    dp[i] = dp[best_j] + b[best_j] * x
    while sz > 1:
        idxA = hull[sz - 2]
        idxB = hull[sz - 1]
        idxC = i
        if (dp[idxB] - dp[idxA]) * (b[idxB] - b[idxC]) >= (dp[idxC] - dp[idxB]) * (b[idxA] - b[idxB]):
            sz -= 1
            if ptr >= sz:
                ptr = sz - 1
        else:
            break
    hull[sz] = i
    sz += 1
sys.stdout.write(str(dp[n - 1]) + '\n')