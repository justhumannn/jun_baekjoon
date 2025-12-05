n = int(input())
files = list(map(int, input().split()))
c = int(input())

total = 0
for s in files:
    if s > 0:
        total += ((s + c - 1) // c) * c

print(total)