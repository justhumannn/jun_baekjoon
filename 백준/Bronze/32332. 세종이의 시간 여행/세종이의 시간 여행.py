from decimal import Decimal, getcontext

getcontext().prec = 20
Y0, M0, D0, T0, P0 = input().split()
Y1, M1, D1, T1, P1 = input().split()
Y0, M0, D0 = map(int, (Y0, M0, D0))
Y1, M1, D1 = map(int, (Y1, M1, D1))
T0, P0 = Decimal(T0), Decimal(P0)
T1, P1 = Decimal(T1), Decimal(P1)
def to_days(y, m, d):
    return y * 360 + (m - 1) * 30 + (d - 1)
C_day = to_days(Y0, M0, D0)
A_day = to_days(Y1, M1, D1)
I_day = 2 * C_day - A_day
Iy = I_day // 360
rem = I_day % 360
Im = rem // 30 + 1
Id = rem % 30 + 1
It = 2 * T0 - T1
Ip = 2 * P0 - P1
print(
    f"{Iy} {Im} {Id} "
    f"{It:.3f} {Ip:.3f}"
)