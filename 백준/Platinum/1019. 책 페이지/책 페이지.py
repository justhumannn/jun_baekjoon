a = int(input())
arr = [0] * 10
num = 1
def make_nine(a):
    while a % 10 != 9:
        for i in str(a):
            arr[int(i)] += num
        a -= 1
    return a
while a > 0:
    a = make_nine(a)
    if a < 10:
        for i in range(a + 1):
            arr[i] += num
    else:
        for i in range(10):
            arr[i] += (a // 10 + 1) * num
    arr[0] -= num
    num *= 10
    a //= 10
print(*arr)