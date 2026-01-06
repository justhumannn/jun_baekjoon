t = int(input())
ns = [int(input()) for _ in range(t)]
max_n = max(ns)
dp = [0] * (max_n + 1)
for i in range(max_n + 1):
    if i < 2:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

for n in ns:
    print(dp[n])