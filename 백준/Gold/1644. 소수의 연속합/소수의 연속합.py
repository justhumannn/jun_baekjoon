a = int(input())
eratos = [True for i in range(a + 1)]
eratos[0] = False
eratos[1] = False
for i in range(2,int(a * 0.5) + 1):
    if eratos[i]:
        for j in range(i*2,a + 1,i):
            eratos[j] = False
prime = []
for i in range(2,a + 1):
    if eratos[i]:
        prime.append(i)
start = 0
end = 1
count = 0
while end <= len(prime):
    sum_num = sum(prime[start:end])
    if sum_num > a:
        start += 1
    elif sum_num < a:
        end += 1
    else:
        count += 1
        start += 1
print(count)