a = int(input())
for _ in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    d = int(input())
    dp = [0] * (d + 1)
    dp[0] = 1
    for i in c:
        for j in range(i, d + 1):
            dp[j] += dp[j - i]
    print(dp[d])