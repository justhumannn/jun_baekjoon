a = int(input())
b = input()
c = []
for i in range(0,a):
    c.append(ord(b[i])-96)
hash_num = 0
for i in range(0,a):
    hash_num += c[i] * 31 ** i
print(hash_num)