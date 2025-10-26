import sys
from math import gcd
input = sys.stdin.readline

n = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SA = sum(A)
SB = sum(B)
g = gcd(SA, SB)

a = SB // g
b = SA // g
print(a, b)