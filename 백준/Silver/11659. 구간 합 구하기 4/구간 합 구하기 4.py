import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num_list = list(map(int,input().split()))
sum_list = [0] * (n+1)
for i in range(n):
    sum_list[i+1] = sum_list[i] + num_list[i]
for _ in range(m):
    a,b = map(int,input().split())
    print(sum_list[b]-sum_list[a-1])