import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.tree = [0] * (self.size << 1)
    def build_all_ones(self):
        for i in range(self.n):
            self.tree[self.size + i] = 1
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]

    def update(self, idx, val):
        node = self.size + idx
        self.tree[node] = val
        node >>= 1
        while node:
            self.tree[node] = self.tree[node << 1] + self.tree[(node << 1) + 1]
            node >>= 1
    def kth(self, k):
        node = 1
        if k < 1 or k > self.tree[1]:
            return -1
        while node < self.size:
            left_sum = self.tree[node << 1]
            if k <= left_sum:
                node = node << 1
            else:
                k -= left_sum
                node = (node << 1) + 1
        return node - self.size
a, b = map(int, input().split())
seg = SegmentTree(a)
seg.build_all_ones()
result = []
c = 0
d = a
for _ in range(a):
    e = (c + b - 1) % d + 1
    idx = seg.kth(e)
    result.append(idx + 1)
    seg.update(idx, 0)
    d -= 1
    c = (e - 1) % (d if d > 0 else 1)
print("<" + ", ".join(map(str, result)) + ">")