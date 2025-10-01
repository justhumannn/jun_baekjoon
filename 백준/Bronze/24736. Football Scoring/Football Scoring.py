a = list(map(int, input().split()))
b = list(map(int, input().split()))
def score(x):
    return 6*x[0] + 3*x[1] + 2*x[2] + x[3] + 2*x[4]
print(score(a), score(b))