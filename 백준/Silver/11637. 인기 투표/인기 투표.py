import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    max_votes = max(votes)
    max_count = votes.count(max_votes)
    total_votes = sum(votes)

    if max_count > 1:
        print("no winner")
    else:
        winner = votes.index(max_votes) + 1
        if max_votes > total_votes // 2:
            print(f"majority winner {winner}")
        else:
            print(f"minority winner {winner}")