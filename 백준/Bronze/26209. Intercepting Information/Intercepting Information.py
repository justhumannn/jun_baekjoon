import sys
a=list(map(int,sys.stdin.readline().split()))
b='F' if 9 in a else 'S'
print(b)
