import sys

tokens = sys.stdin.read().split()
d = int(tokens[0])
p = int(tokens[1])
q = int(tokens[2])
if p < q:
    p, q = q, p
ans = float('inf')
limit = min(q, d // p + 1)
for x in range(limit + 1):
    rem = d - x * p
    if rem <= 0:
        y = 0
    else:
        y = (rem + q - 1) // q
    val = x * p + y * q
    if val < ans:
        ans = val
print(ans)