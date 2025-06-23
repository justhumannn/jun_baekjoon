a = int(input())
b = int(input())
e = [b]
for i in range(a):
    c,d = map(int,input().split())
    b += c-d
    e.append(b)
if min(e) < 0:
    print(0)
else:
    print(max(e))