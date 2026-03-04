N, P, S = map(int, input().split())
for _ in range(S):
    line = list(map(int, input().split()))
    m = line[0]
    chosen_cards = line[1:]
    if P in chosen_cards:
        print("KEEP")
    else:
        print("REMOVE")