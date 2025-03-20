a = int(input())
count = []
b = list(map(int,input().split()))
c = 0
for i in range(0,a):
    count.append(0)
    j = 2
    while True:
        if b[i] == 1:
            break
        elif j == b[i]:
            break
        elif b[i] % j != 0:
            count[i] += 1
        j += 1
    if count[i] == b[i] - 2:
        c += 1
print(c)
            