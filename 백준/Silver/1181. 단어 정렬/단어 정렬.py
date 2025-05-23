a = int(input())
b = []
for i in range(a):
    b.append(input())
c = [[]for i in range(51)]
for i in b:
    c[len(i)].append(i)
for i in range(len(c)):
    c[i].sort()
d = []

for i in c:
    for j in i:
        if j not in d:
            d.append(j)
for i in d:
    print(i)