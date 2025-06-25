a,b = map(int,input().split())
password = dict()
for _ in range(a):
    c,d = input().split()
    password[c] = d
for _ in range(b):
    c = input()
    print(password[c])