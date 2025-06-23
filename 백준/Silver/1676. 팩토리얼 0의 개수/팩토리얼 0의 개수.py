def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
a = int(input())
b = fact(a)
b = str(b)
c = 0
for i in range(-1,-len(b)+1,-1):
    if b[i] != '0':
        break
    c += 1
print(c)