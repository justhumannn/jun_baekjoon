import math

n = int(input())
res = 2 * math.sqrt(n * math.pi)
print(math.ceil(res * 10) / 10)