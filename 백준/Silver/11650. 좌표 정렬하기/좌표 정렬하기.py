a = int(input())
b = []
for _ in range(a):
    b.append(list(map(int,input().split())))
b.sort()
for i in range(0,a):
    print(b[i][0], b[i][1])