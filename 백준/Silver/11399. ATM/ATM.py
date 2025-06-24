a = int(input())
b = list(map(int,input().split()))
b.sort()
total = 0
for i in range(len(b)-1):
    b[i+1] += b[i]
for i in b:
    total += i
print(total)