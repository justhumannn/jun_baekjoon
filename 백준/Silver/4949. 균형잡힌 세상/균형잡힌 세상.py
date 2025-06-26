import sys
input = sys.stdin.readline
a = input()
while a != '.\n':
    stacklist = []
    check = 0
    for i in a:
        if i == '(' or i == '[':
            stacklist.append(i)
        elif i == ')':
            if len(stacklist) > 0 and stacklist[-1] == '(':
                stacklist.pop()
            else:
                print('no')
                check = 1
                break
        elif i == ']':
            if len(stacklist) > 0 and stacklist[-1] == '[':
                stacklist.pop()
            else:
                print('no')
                check = 1
                break
    if check == 0:
        if len(stacklist) == 0:
            print('yes')
        else:
            print('no')
    a = input()