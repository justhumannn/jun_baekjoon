n, m = map(int, input().split())
total_minutes = 24 * 60
current_minutes = (m * total_minutes) // n
hh = current_minutes // 60
mm = current_minutes % 60
print(f"{hh:02}:{mm:02}")