a = int(input())
b = list(map(int,input().split()))
new = 0
max_b = max(b)
for i in range(0,a):
    new += b[i] / max_b * 100
new /= a
print(new)