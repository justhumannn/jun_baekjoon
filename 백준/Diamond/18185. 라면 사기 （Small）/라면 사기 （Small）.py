import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().split())) + [0,0]
money = 0

def buy1(i):
    money = b[i] * 3
    return money
def buy2(i):
    min_num = min(b[i],b[i+1])
    if min_num == 0:
        return 0
    b[i] -= min_num
    b[i+1] -= min_num
    money = min_num * 5
    return money
def buy3(i):
    min_num = min(b[i],b[i+1],b[i+2])
    if min_num == 0:
        return 0
    b[i] -= min_num
    b[i+1] -= min_num
    b[i+2] -= min_num
    money = min_num * 7
    return money

for i in range(a):
    if b[i] == 0:
        continue
    if b[i+1] > b[i+2]:
        min_num = min(b[i],b[i+1]-b[i+2])
        b[i] -= min_num
        b[i+1] -= min_num
        money += 5 * min_num
        money += buy3(i)
        money += buy1(i)
    else:
        money += buy3(i)
        money += buy2(i)
        money += buy1(i)
print(money)