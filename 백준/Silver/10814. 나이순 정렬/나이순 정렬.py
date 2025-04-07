a = int(input())
b = []
for i in range(0,a):
    b.append(list(input().split()))
    b[i][0] = int(b[i][0])
b.sort(key=lambda x: x[0])
for i in range(0,a):
    print(b[i][0],b[i][1])