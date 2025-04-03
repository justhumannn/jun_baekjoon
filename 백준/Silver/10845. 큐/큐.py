quene = [0]*10001
front,rear = -1,-1
import sys
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    b = list(map(str,input().split()))
    if b[0] == "front":
        if front != rear:
            print(quene[front+1])
        else:
            print(-1)
    elif b[0] == 'back':
        if front != rear:
            print(quene[rear])
        else:
          print(-1)
    elif b[0] == 'pop':
        if front != rear:
            front += 1
            print(quene[front])
            quene[front] = 0
        else:
            print(-1)
    elif b[0] == 'size':
        print(rear-front)
    elif b[0] == 'empty':
        if rear == front:
            print(1)
        else:
            print(0)
    else:
        rear += 1
        quene[rear] = b[1]