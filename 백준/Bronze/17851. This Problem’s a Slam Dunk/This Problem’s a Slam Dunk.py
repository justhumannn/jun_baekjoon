state = list(map(int, input().split()))
ustate = list(map(int, input().split()))
state.sort(reverse=True)
ustate.sort(reverse=True)
count = 0
for s, u in zip(state, ustate):
    if s > u:
        count += 1
print(count)