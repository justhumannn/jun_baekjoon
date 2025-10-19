import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

mx = 0
for i, ti in enumerate(t, start=1):
    mx = max(mx, ti + i)

print(mx + 1)