a = set(range(1, 31))
for _ in range(28):
    a.remove(int(input()))
a = sorted(a)
print(a[0])
print(a[1])