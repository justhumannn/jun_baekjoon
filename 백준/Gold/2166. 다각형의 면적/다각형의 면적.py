import sys
input=sys.stdin.readline
a=int(input())
b=[]
for _ in range(a):
    c,d=map(int,input().split())
    b.append((c,d))
e=0
for f in range(a):
    g,h=b[f]
    i,j=b[(f+1)%a]
    e+=g*j-h*i
k=abs(e)/2
print(f"{k:.1f}")