import sys
import re
from array import array

text = sys.stdin.read()
tokens = (int(match.group()) for match in re.finditer(r'-?\d+', text))
n = next(tokens)
a = next(tokens)
b = next(tokens)
c = next(tokens)
m = array('q', [0]) * (n + 1)
k = array('q', [0]) * (n + 1)
head = 0
tail = 1
s = 0
dp = 0
for _ in range(n):
    s += next(tokens)
    x = s
    while tail - head >= 2:
        if k[head] - k[head+1] <= x * (m[head+1] - m[head]):
            head += 1
        else:
            break
    dp = m[head] * x + k[head] + a * x * x + b * x + c
    new_m = -2 * a * x
    new_k = dp + a * x * x - b * x
    while tail - head >= 2:
        dy1 = k[tail-2] - k[tail-1]
        dx1 = m[tail-1] - m[tail-2]
        dy2 = k[tail-1] - new_k
        dx2 = new_m - m[tail-1]
        if dy1 * dx2 >= dy2 * dx1:
            tail -= 1
        else:
            break
    m[tail] = new_m
    k[tail] = new_k
    tail += 1
print(dp)