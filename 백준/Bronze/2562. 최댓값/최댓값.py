a = []
for _ in range(9):
    a.append(int(input()))
print(max(a))
b = a.index(max(a)) + 1
print(b)