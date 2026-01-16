import sys

input = sys.stdin.read().split()
s = list(input[0])
t = int(input[1])
idx = 2
for _ in range(t):
    a = int(input[idx])
    b = int(input[idx + 1])
    s[a], s[b] = s[b], s[a]
    idx += 2
print("".join(s))