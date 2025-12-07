n = int(input())
mp = {}
for c in "ABC": mp[c] = '2'
for c in "DEF": mp[c] = '3'
for c in "GHI": mp[c] = '4'
for c in "JKL": mp[c] = '5'
for c in "MNO": mp[c] = '6'
for c in "PQRS": mp[c] = '7'
for c in "TUV": mp[c] = '8'
for c in "WXYZ": mp[c] = '9'

for _ in range(n):
    s = input().upper()
    num = ""
    for c in s:
        num += mp[c]
    if num == num[::-1]:
        print("YES")
    else:
        print("NO")