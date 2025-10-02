a = int(input())
for _ in range(a):
    nums = input().split()
    print(" ".join(nums))
    has_mack = "18" in nums
    has_zack = "17" in nums
    if has_mack and has_zack:
        print("both")
    elif has_mack:
        print("mack")
    elif has_zack:
        print("zack")
    else:
        print("none")
    print()