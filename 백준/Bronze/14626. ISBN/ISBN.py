a = list(input())
b = [1, 3] * 6 + [1]
c = a.index('*')

for i in range(10):
    a[c] = str(i)
    total = 0
    for j in range(13):
        total += int(a[j]) * b[j]
    if total % 10 == 0:
        print(i)
        break