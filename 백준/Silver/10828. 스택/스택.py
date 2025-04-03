import sys
input = sys.stdin.readline
a = int(input())
top = -1
c = []
def empty(insert):
    if insert == -1:
        return 1
    return 0
for _ in range(a):
    b = list(map(str,input().split()))
    if b[0] == 'top':
        if top != -1:
            print(c[top])
        else:
            print(top)
    elif b[0] == 'size':
        print(top+1)
    elif b[0] == 'empty':
        print(empty(top))
    elif b[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            top -= 1
            print(c.pop())
    else:
        top += 1
        c.append(b[1])