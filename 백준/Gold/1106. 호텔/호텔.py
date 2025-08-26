a,b = map(int,input().split())
stuff = []
for _ in range(b):
    w,v = map(int,input().split())
    stuff.append((w,v))
dp = [10**10] * (a +100)
dp[0] = 0
for i,j in stuff:
    for k in range(j,a+100):
        dp[k] = min(dp[k],dp[k-j] + i)
print(min(dp[a:]))