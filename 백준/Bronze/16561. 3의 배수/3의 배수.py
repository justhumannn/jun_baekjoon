n = int(input())
m = n // 3
count = 0
for a in range(1, m - 1):
    for b in range(1, m - a):
        c = m - a - b
        if c >= 1:
            count += 1
print(count)