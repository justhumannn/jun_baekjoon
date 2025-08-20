a,b = map(int,input().split())
min_pack = 1000
min_single = 1000
for i in range(b):
    c,d = map(int,input().split())
    if c < min_pack: min_pack = c
    if d < min_single: min_single = d
pack1 = (a+5) // 6 * min_pack
pack2 = min_single * a
pack3 = a // 6 * min_pack + (a % 6) * min_single
min_pack = pack1
if pack2 < min_pack: min_pack = pack2
if pack3 < min_pack: min_pack = pack3
print(min_pack)