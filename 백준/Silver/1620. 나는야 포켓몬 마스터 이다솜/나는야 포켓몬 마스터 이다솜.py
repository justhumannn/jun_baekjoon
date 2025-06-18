import sys
input = sys.stdin.readline
a,b = map(int,input().split())
dict = []
dict2 = {}
i = 1
for _ in range(a):
    c = input().strip()
    dict2[c] = i
    i += 1
    dict.append(c)
problem = []
for _ in range(b):
    c = input().strip()
    if c.isdigit():
        c = int(c)
    problem.append(c)
for i in problem:
    if type(i) == int:
        print(dict[i-1])
    else:
        print(dict2[i])
