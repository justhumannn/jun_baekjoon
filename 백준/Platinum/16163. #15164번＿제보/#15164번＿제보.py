import sys

s = sys.stdin.read().split()
t = '^#' + '#'.join(s[0]) + '#$'
n = len(t)
p = [0] * n
c = 0
r = 0
ans = 0
for i in range(1, n - 1):
    if r > i:
        pi = p[2 * c - i]
        diff = r - i
        if pi > diff:
            pi = diff
    else:
        pi = 0
    while t[i - 1 - pi] == t[i + 1 + pi]:
        pi += 1
    p[i] = pi
    if i + pi > r:
        c = i
        r = i + pi
    ans += (pi + 1) >> 1
print(ans)