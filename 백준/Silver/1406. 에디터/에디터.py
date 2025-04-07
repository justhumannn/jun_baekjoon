import sys
input = sys.stdin.readline
a = list(input())
a.pop()
b = int(input())
c = []
for _ in range(b):
    command = list(map(str,input().split()))
    if command[0] == 'L':
        if len(a) != 0:
            c.append(a.pop())
    elif command[0] == 'D':
        if len(c) != 0:
            a.append(c.pop())
    elif command[0] == 'B':
        if len(a) != 0:
            a.pop()
    else:
        a.append(command[1])
print(''.join(a)+''.join(reversed(c)))