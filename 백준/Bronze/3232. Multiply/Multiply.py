T = int(input())
for _ in range(T):
    p_str, q_str, r_str = input().split()
    max_digit = 0
    for s in [p_str, q_str, r_str]:
        for char in s:
            max_digit = max(max_digit, int(char))
    ans = 0
    for b in range(max(2, max_digit + 1), 17):
        p_val = int(p_str, b)
        q_val = int(q_str, b)
        r_val = int(r_str, b)
        
        if p_val * q_val == r_val:
            ans = b
            break
    print(ans)