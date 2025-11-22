n = int(input().strip())
s1 = input().strip()
s2 = input().strip()

count = 0
for a, b in zip(s1, s2):
    if a == b:
        count += 1

print(count)