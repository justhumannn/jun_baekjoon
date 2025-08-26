a = int(input())
cost = [list(map(int, input().split())) for _ in range(a)]
ans = float('inf')
for first in range(3):
    dp = [[10**9] * 3 for _ in range(a)]
    dp[0][first] = cost[0][first]
    for i in range(1, a):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    for last in range(3):
        if first != last:
            ans = min(ans, dp[a-1][last])
print(ans)