a,b = map(int, input().split())
len_line = []
for i in range(a):
    len_line.append(int(input()))
len_line.sort()
count_list = []
def binary_search(start, end):
    count = 0
    while start <= end:
        mid = (start + end) // 2
        for j in len_line:
            count += j // mid
        if count >= b:
            count_list.append(mid)
            start = mid + 1
        elif count < b:
            end = mid - 1
        else:
            start = mid + 1
        count = 0
binary_search(1, len_line[-1])
print(max(count_list))