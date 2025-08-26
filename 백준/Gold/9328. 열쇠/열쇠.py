from collections import deque
import sys

input=sys.stdin.readline
a=int(input())
while a:
    a-=1
    b,c=map(int,input().split())
    d=[list(input().rstrip()) for _ in range(b)]
    e=list(input().strip())
    if e==['0']: e=[]
    f=[['.' for _ in range(c+2)] for __ in range(b+2)]
    for g in range(b):
        for h,ch in enumerate(d[g],1):
            f[g+1][h]=ch
    w=[[False]*(c+2) for _ in range(b+2)]
    q=deque()
    i={x:[] for x in "abcdefghijklmnopqrstuvwxyz"}
    j=0
    q.append((0,0))
    w[0][0]=True
    while q:
        y,x=q.popleft()
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny,nx=y+dy,x+dx
            if ny<0 or ny>b+1 or nx<0 or nx>c+1: continue
            if w[ny][nx]: continue
            ch=f[ny][nx]
            if ch=='*': continue
            if 'A'<=ch<='Z':
                if ch.lower() not in e:
                    i[ch.lower()].append((ny,nx))
                    continue
            w[ny][nx]=True
            if 'a'<=ch<='z':
                if ch not in e:
                    e.append(ch)
                    for yy,xx in i[ch]:
                        w[yy][xx]=True
                        q.append((yy,xx))
            if ch=='$':
                j+=1
                f[ny][nx]='.'
            q.append((ny,nx))
    print(j)
