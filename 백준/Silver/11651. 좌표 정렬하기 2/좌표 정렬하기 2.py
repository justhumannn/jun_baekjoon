a = int(input())
b = []
for i in range(0,a):
    b.append(list(map(int,input().split())))
    b[i].reverse()
b.sort()
for i in range(0,a):
    print(b[i][1], b[i][0])