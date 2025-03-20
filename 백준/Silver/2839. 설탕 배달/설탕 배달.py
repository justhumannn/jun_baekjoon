a = int(input())
b = 0
while True:
    if a <= 0:
        # print(a,b)
        break
    elif a % 5 == 0:
        b += a // 5
        # print(a,b)
        break
    elif a < 5:
        if a % 3 != 0:
            b = -1
            # print(a,b)
            break
        else:
            a -= 3
            b += 1
            # print(a,b)
    elif a % 5 == 3:
        b += (a // 5) + 1
        # print(a,b)
        break
    else:
        a -= 3
        b += 1
        # print(a,b)
print(b)