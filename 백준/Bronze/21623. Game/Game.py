import sys
input = sys.stdin.readline

k, n = map(int, input().split())
a = list(map(int, input().split()))
score = n
rounds = 0
for i in range(k):
    if a[i] <= score:
        score -= a[i]
    if score == 0:
        rounds += 1
        if i != k - 1:
            score = n
print(rounds)
print(score)