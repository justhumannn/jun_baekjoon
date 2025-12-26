import sys
input = sys.stdin.readline

n = int(input())
cnt = [0] * 26
for _ in range(n):
    name = input()
    cnt[ord(name[0]) - ord('a')] += 1
result = []
for i in range(26):
    if cnt[i] >= 5:
        result.append(chr(i + ord('a')))
if result:
    print(''.join(result))
else:
    print("PREDAJA")