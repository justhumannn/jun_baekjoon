import sys

input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def intersect(p1, p2, p3, p4):
    c1 = ccw(p1, p2, p3)
    c2 = ccw(p1, p2, p4)
    c3 = ccw(p3, p4, p1)
    c4 = ccw(p3, p4, p2)
    
    if c1 * c2 == 0 and c3 * c4 == 0:
        if min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and \
           min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1]):
            return True
        return False
    return c1 * c2 <= 0 and c3 * c4 <= 0

def get_hull(points):
    points = sorted(list(set(points)))
    if len(points) <= 2:
        return points
    
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
        
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
        
    return lower[:-1] + upper[:-1]

def in_poly(p, poly):
    if len(poly) < 3:
        return False
    cnt = 0
    for i in range(len(poly)):
        p1 = poly[i]
        p2 = poly[(i+1)%len(poly)]
        if p1[1] > p2[1]:
            p1, p2 = p2, p1
        if p1[1] <= p[1] < p2[1] and ccw(p1, p2, p) > 0:
            cnt += 1
    return cnt % 2 == 1

T = int(input().strip())

for _ in range(T):
    n, m = map(int, input().split())
    
    A = []
    for _ in range(n):
        A.append(tuple(map(int, input().split())))
        
    B = []
    for _ in range(m):
        B.append(tuple(map(int, input().split())))
        
    ha = get_hull(A)
    hb = get_hull(B)
    
    possible = True
    for i in range(len(ha)):
        p1 = ha[i]
        p2 = ha[(i+1)%len(ha)]
        for j in range(len(hb)):
            p3 = hb[j]
            p4 = hb[(j+1)%len(hb)]
            if intersect(p1, p2, p3, p4):
                possible = False
                break
        if not possible:
            break
            
    if possible:
        if len(hb) >= 3 and in_poly(ha[0], hb):
            possible = False
        elif len(ha) >= 3 and in_poly(hb[0], ha):
            possible = False
            
    if possible:
        print("YES")
    else:
        print("NO")