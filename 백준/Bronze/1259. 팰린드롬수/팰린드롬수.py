while True:
    a = input()
    if int(a) == 0:
        break
    b = len(a) // 2
    if len(a) % 2 == 0:
        c = ''.join(reversed(a[b:len(a)+1]))
        if a[0:b] == c:
            print('yes')
        else:
            print('no')
    else:
        c = ''.join(reversed(a[b+1:len(a)+1]))
        if a[0:b] == c:
            print('yes')
        else:
            print('no')
        