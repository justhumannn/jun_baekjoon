a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in b:
    print(dp[i])