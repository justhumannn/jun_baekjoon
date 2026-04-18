import sys
input = sys.stdin.readline

n = int(input())
match = [0] * 101
for _ in range(n):
    u, v = map(int, input().split())
    match[u] = v
    match[v] = u
dp = [[0] * 101 for _ in range(101)]
for length in range(2, 101):
    for i in range(1, 101 - length + 1):
        j = i + length - 1
        dp[i][j] = dp[i][j-1]
        k = match[j]
        if k != 0 and i <= k < j:
            val = 1
            if k > i:
                val += dp[i][k-1]
            if k + 1 < j:
                val += dp[k+1][j-1]
            
            if val > dp[i][j]:
                dp[i][j] = val
sys.stdout.write(str(dp[1][100]) + '\n')