a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
b.sort(reverse=True)
result = 0
for _ in range(a):
    max_num = 0
    d = b.pop()
    for i in c:
        if max_num < i:
            max_num = i
    result += d * max_num
    c.pop(c.index(max_num))
print(result)