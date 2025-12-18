n = int(input())
count = 0
if n <= 5:
    count += 1
for a in range(1, 6):
    for b in range(1, a + 1):
        if a + b == n:
            count += 1
print(count)