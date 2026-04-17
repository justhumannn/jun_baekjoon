import sys
import math
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
k = int(input())
mod_val = [int(x) % k for x in arr]
p10_len = [(10 ** len(x)) % k for x in arr]
next_r = [[(rem * p10_len[i] + mod_val[i]) % k for rem in range(k)] for i in range(n)]
dp = [[0] * k for _ in range(1 << n)]
dp[0][0] = 1
for mask in range(1 << n):
    for rem, cnt in enumerate(dp[mask]):
        if not cnt:
            continue
        for i in range(n):
            if not (mask & (1 << i)):
                dp[mask | (1 << i)][next_r[i][rem]] += cnt
p = dp[(1 << n) - 1][0]
q = math.factorial(n)
g = math.gcd(p, q)
sys.stdout.write(f"{p // g}/{q // g}\n")