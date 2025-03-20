a,b = map(int,input().split())
c = list(map(int,input().split()))
count = []
for i in range(0,a):
    if c[i] < b:
        count.append(c[i])
        count.append(' ')
count[0] = str(count[0])
for i in range(1,len(count)-1):
    count[i] = str(count[i])
    count[0] += count[i]
print(count[0])