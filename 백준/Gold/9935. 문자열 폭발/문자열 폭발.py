a = input()
b = input()
stack = []
for i in a:
    stack.append(i)
    if ''.join(stack[-len(b):]) == b:
        del stack[-len(b):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')