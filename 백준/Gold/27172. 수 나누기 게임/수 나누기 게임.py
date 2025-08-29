a = int(input())
b = list(map(int, input().split()))
exists = [False] * (1000000 + 1)
score = [0] * (1000000 + 1)
for i in b:
    exists[i] = True
for i in b:
    j = i * 2
    while j <= 1000000:
        if exists[j]:
            score[i] += 1
            score[j] -= 1
        j += i
print(" ".join(str(score[i]) for i in b))