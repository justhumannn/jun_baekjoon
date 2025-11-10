import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = int(input())
b = {}
for _ in range(a):
    c = input().split()
    d = c[1:]
    e = b
    for f in d:
        if f not in e:
            e[f] = {}
        e = e[f]
def print_trie(g, h):
    i = sorted(g.keys())
    for j in i:
        print("--" * h + j)
        print_trie(g[j], h + 1)
print_trie(b, 0)