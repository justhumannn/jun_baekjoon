a = int(input())
from collections import deque
for _ in range(a):
    p = input()
    n = int(input())
    li = input()
    if n == 0:
        li2 = deque()
    else:
        li = li[1:-1].split(',')
        li2 = deque(map(int, li))
    reverse = 0
    error = False
    for i in p:
        if i == 'R':
            reverse += 1
        else:
            if len(li2) == 0:
                print('error')
                error = True
                break
            if reverse % 2 == 0:
                li2.popleft()
            else:
                li2.pop()
    if not error:
        if reverse % 2 == 1:
            li2.reverse()
        print(f"[{','.join(map(str, li2))}]")