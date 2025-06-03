import sys

input = sys.stdin.readline
write = sys.stdout.write

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        write(str(a + b) + '\n')

if __name__ == "__main__":
    main()
