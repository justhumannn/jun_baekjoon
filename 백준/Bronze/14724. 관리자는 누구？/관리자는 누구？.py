import sys

clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit(0)

N = data[0]
vals = data[1:]

best_scores = []
idx = 0
for _ in range(9):
    group = vals[idx: idx + N]
    idx += N
    best_scores.append(max(group))

best_idx = max(range(9), key=lambda i: best_scores[i])
print(clubs[best_idx])