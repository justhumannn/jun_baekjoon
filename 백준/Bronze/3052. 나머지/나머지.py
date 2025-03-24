a = []
for _ in range(10):
    b = int(input())
    a.append(b%42)
b = set(a)
print(len(b))