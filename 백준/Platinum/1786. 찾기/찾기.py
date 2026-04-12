import sys
input = sys.stdin.readline

a = input()[:-1] 
b = input()[:-1]
n = len(a)
m = len(b)
pi = [0] * m
j = 0
for i in range(1, m):
    while j > 0 and b[i] != b[j]:
        j = pi[j - 1]
    if b[i] == b[j]:
        j += 1
        pi[i] = j
ans = []
j = 0
for i in range(n):
    while j > 0 and a[i] != b[j]:
        j = pi[j - 1]
    if a[i] == b[j]:
        if j == m - 1:
            ans.append(i - m + 2)
            j = pi[j]
        else:
            j += 1
print(len(ans))
if ans:
    print(*ans)