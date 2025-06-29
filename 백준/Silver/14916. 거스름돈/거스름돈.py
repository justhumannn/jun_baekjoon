a = int(input())
count = -1
for i in range(a//5, -1, -1):
    b = a - (i*5)
    if b % 2 == 0:
        c = b // 2
        count = i+c
        break
print(count)