a = int(input())
c = []
for _ in range(a):
    d = 0
    b = list(input())
    for i in range(0,len(b)):
        if b[i] == '(':
            c.append('(')
        else:
            if c == []:
                d = 1
                print('NO')
                break
            c.pop()
    if d != 1:
        if c == []:
            print('YES')
        else:
            print('NO')
            c = []