a = int(input())
b = int(input())
c = int(input())
d = a * b * c
d = str(d)
for i in range(0,10):
    i = str(i)
    print(d.count(i))