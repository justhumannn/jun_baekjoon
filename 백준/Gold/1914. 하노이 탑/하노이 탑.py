def hanoi(n,start,end,temp):
    if n == 1:
        print(start,end)
        return
    hanoi(n-1,start,temp,end)
    print(start,end)
    hanoi(n-1,temp,end,start)
    
a = int(input())
print(2**a - 1)
if a <= 20:
    hanoi(a,1,3,2)