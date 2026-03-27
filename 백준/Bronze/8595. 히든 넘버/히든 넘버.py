import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()
total_sum = 0
current_num = 0
is_counting = False
for char in word:
    if char.isdigit():
        current_num = current_num * 10 + int(char)
        is_counting = True
    else:
        if is_counting:
            total_sum += current_num
            current_num = 0
            is_counting = False
if is_counting:
    total_sum += current_num

print(total_sum)