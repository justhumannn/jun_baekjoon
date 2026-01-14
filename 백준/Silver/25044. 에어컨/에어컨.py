import sys
input = sys.stdin.readline

line = input().split()
if line:
    n, k = map(int, line)
    minutes_per_day = 1440
    cycle_len = 1440 + k
    day_start = n * minutes_per_day
    day_end = (n + 1) * minutes_per_day
    valid_times = []
    estimated_cycle = day_start // cycle_len
    for cycle in range(estimated_cycle - 1, estimated_cycle + 3):
        if cycle < 0:
            continue
        base_time = cycle * cycle_len
        offsets = [900, 1080, 1260]
        for offset in offsets:
            event_real_time = base_time + offset
            
            if day_start <= event_real_time < day_end:
                current_day_minutes = event_real_time % minutes_per_day
                hh = current_day_minutes // 60
                mm = current_day_minutes % 60
                valid_times.append((hh, mm))
    valid_times.sort()
    print(len(valid_times))
    for h, m in valid_times:
        print(f"{h:02d}:{m:02d}")