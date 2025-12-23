import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = {}
for _ in range(N):
    for x in map(int, input().split()):
        cnt[x] = cnt.get(x, 0) + 1
odd = 0
for v in cnt.values():
    if v % 2 == 1:
        odd += 1
if M % 2 == 0:
    print("YES" if odd == 0 else "NO")
else:
    print("YES" if odd <= N else "NO")