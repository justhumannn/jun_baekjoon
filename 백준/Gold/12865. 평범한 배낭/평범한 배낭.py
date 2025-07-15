a,b = map(int,input().split())
stuff = []
for _ in range(a):
    w,v = map(int,input().split())
    stuff.append((w,v))
dp = [[0] * (b + 1) for _ in range(a + 1)]
for i in range(1, a + 1):
    w, v = stuff[i - 1]
    for j in range(b + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[a][b])