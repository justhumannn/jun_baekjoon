import sys

n = int(sys.stdin.readline())
c = [[0] * 53 for _ in range(53)]
for i in range(53):
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = (c[i-1][j-1] + c[i-1][j]) % 10007
total_ways = c[52][n]
dp = [0] * 53
dp[0] = 1
ways = (1, 4, 6, 4)
for _ in range(13):
    next_dp = [0] * 53
    for j in range(53):
        if dp[j]:
            for k in range(4):
                if j + k <= 52:
                    next_dp[j + k] = (next_dp[j + k] + dp[j] * ways[k]) % 10007
    dp = next_dp
print((total_ways - dp[n] + 10007) % 10007)