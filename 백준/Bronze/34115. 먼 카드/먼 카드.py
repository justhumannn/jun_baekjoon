import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
pos = [[] for _ in range(N + 1)]
for i in range(2 * N):
    pos[X[i]].append(i)
answer = 0
for k in range(1, N + 1):
    l, r = pos[k]
    answer = max(answer, r - l - 1)
print(answer)