import sys
import math

n = int(sys.stdin.readline())
ans = 1
for _ in range(n):
    x = int(sys.stdin.readline())
    ans = (ans * x) // math.gcd(ans, x)
print(ans)