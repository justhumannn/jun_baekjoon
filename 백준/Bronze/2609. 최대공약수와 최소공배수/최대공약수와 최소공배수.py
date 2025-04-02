a,b = map(int,input().split())
max_div = 1
for i in range(2,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        max_div = max(max_div,i)
print(max_div)
def test(b,c):
    while c != 0:
        b,c = c, b%c
    return b
if a > b:
    c = test(a,b)
else:
    c = test(b,a)
print((a*b) // c)