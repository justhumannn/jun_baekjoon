n = int(input())
a = list(map(int, input().split()))
b = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            b[i] = max(b[i], b[j] + 1)
print(max(b))