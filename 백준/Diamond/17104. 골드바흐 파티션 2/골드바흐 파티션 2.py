import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

T = int(input_data[0])
queries = [int(x) for x in input_data[1:T+1]]

is_prime = bytearray([1]) * 1000001
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, 1001):
    if is_prime[i]:
        is_prime[i*i::i] = bytearray([0]) * len(is_prime[i*i::i])

MOD = 998244353
W = 3
sz = 2097152

a = [0] * sz
for i in range(1000001):
    if is_prime[i]:
        a[i] = 1

def ntt(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    
    length = 2
    while length <= n:
        half = length >> 1
        wlen = pow(W, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        
        w_arr = [1] * half
        for i in range(1, half):
            w_arr[i] = (w_arr[i-1] * wlen) % MOD
            
        for i in range(0, n, length):
            for j in range(half):
                u = a[i + j]
                v = (a[i + j + half] * w_arr[j]) % MOD
                a[i + j] = (u + v) % MOD
                a[i + j + half] = (u - v) % MOD
        length <<= 1
        
    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = (a[i] * inv_n) % MOD

ntt(a, False)
for i in range(sz):
    a[i] = (a[i] * a[i]) % MOD
ntt(a, True)

out = []
for n in queries:
    ans = a[n]
    if is_prime[n >> 1]:
        ans += 1
    out.append(str(ans >> 1))

sys.stdout.write('\n'.join(out) + '\n')