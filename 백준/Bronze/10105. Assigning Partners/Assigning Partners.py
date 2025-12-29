N = int(input())
A = input().split()
B = input().split()
idx = {name: i for i, name in enumerate(A)}
good = True
for i in range(N):
    if A[i] == B[i]:
        good = False
        break
    partner_idx = idx[B[i]]
    if B[partner_idx] != A[i]:
        good = False
        break
print("good" if good else "bad")