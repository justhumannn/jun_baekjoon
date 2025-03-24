def test(a,b,c):
    while b != 'z':
        c = c + str(a.find(b)) + ' '
        b = ord(b)
        b += 1
        b = chr(b)
    c += str(a.find(b))
    return c
a = input()
c = ''
print(test(a,'a',c))