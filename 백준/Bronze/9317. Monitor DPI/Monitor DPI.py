import sys
import math

sqrt_337 = math.sqrt(337)

for line in sys.stdin:
    try:
        parts = line.split()
        if not parts:
            continue 
            
        d = float(parts[0])
        rh = int(parts[1])
        rv = int(parts[2])
    except (ValueError, IndexError):
        break

    if d == 0 and rh == 0 and rv == 0:
        break

    w = (16 * d) / sqrt_337
    h = (9 * d) / sqrt_337

    dpi_h = rh / w
    dpi_v = rv / h

    print(f"Horizontal DPI: {dpi_h:.2f}")
    print(f"Vertical DPI: {dpi_v:.2f}")