from itertools import combinations

N = int(input())
winner = 0
max_mod = -1
for i in range(1, N + 1):
    cards = list(map(int, input().split()))
    best = 0
    for comb in combinations(cards, 3):
        s = sum(comb) % 10
        if s > best:
            best = s
    if best >= max_mod:
        max_mod = best
        winner = i
print(winner)