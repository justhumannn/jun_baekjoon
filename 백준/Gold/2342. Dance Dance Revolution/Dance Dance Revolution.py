import sys

moves = list(map(int, sys.stdin.read().split()))
if moves and moves[-1] == 0:
    moves.pop()
if not moves:
    print(0)
else:
    cost = (
        (1, 2, 2, 2, 2),
        (2, 1, 3, 4, 3),
        (2, 3, 1, 3, 4),
        (2, 4, 3, 1, 3),
        (2, 3, 4, 3, 1)
    )
    dp = [[400001] * 5 for _ in range(5)]
    dp[0][0] = 0
    for target in moves:
        next_dp = [[400001] * 5 for _ in range(5)]
        for l in range(5):
            for r in range(5):
                if dp[l][r] != 400001:
                    if target != r:
                        n_cost = dp[l][r] + cost[l][target]
                        if n_cost < next_dp[target][r]:
                            next_dp[target][r] = n_cost
                            
                    if target != l:
                        n_cost = dp[l][r] + cost[r][target]
                        if n_cost < next_dp[l][target]:
                            next_dp[l][target] = n_cost    
        dp = next_dp
    min_power = 400001
    for l in range(5):
        for r in range(5):
            if dp[l][r] < min_power:
                min_power = dp[l][r]
    print(min_power)