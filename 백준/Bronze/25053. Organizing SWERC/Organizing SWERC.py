t = int(input())

for _ in range(t):
    n = int(input())
    max_beauty = [-1] * 11
    for _ in range(n):
        b, d = map(int, input().split())
        if b > max_beauty[d]:
            max_beauty[d] = b
    possible = True
    total_beauty = 0
    for i in range(1, 11):
        if max_beauty[i] == -1:
            possible = False
            break
        total_beauty += max_beauty[i]
    if possible:
        print(total_beauty)
    else:
        print("MOREPROBLEMS")