a = int(input())
if a <= 99:
    print(a)
elif a <= 110:
    print(99)
else:
    b = 99
    for i in range(111,a+1):
        if i // 100 - i % 100 // 10 == i % 100 // 10 - i % 10:
            b += 1
    print(b)