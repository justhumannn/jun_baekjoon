a = list(input())
b = [1,0,0]
for i in a:
    if i == 'A':
        b[0], b[1] = b[1],b[0]
    elif i == 'B':
        b[1],b[2] = b[2],b[1]
    else:
        b[0],b[2] = b[2], b[0]
if b[0] == 1:
    print(1)
elif b[1] == 1:
    print(2)
else:
    print(3)