h_angle, m_angle = map(int, input().split())
if (h_angle % 30) * 12 == m_angle:
    print("O")
else:
    print("X")