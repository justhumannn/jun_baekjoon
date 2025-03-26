a = [0,1]
b = int(input())
for i in range(0,b-1):
    a.append(a[i] + a[i+1])
print(a[b])