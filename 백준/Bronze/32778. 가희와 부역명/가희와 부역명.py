s = input()
if '(' in s:
    p = s.split('(')
    print(p[0].strip())
    print(p[1][:-1])
else:
    print(s)
    print('-')