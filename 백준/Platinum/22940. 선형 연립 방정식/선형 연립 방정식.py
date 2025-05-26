def gaussian_elimination(mat, n):
    # 전진 소거 (Forward Elimination)
    for i in range(n):
        # 피벗 정렬
        max_row = i
        for j in range(i + 1, n):
            if abs(mat[j][i]) > abs(mat[max_row][i]):
                max_row = j
        mat[i], mat[max_row] = mat[max_row], mat[i]

        # i번째 열 기준 소거
        for j in range(i + 1, n):
            ratio = mat[j][i] / mat[i][i]
            for k in range(i, n + 1):
                mat[j][k] -= ratio * mat[i][k]

    # 역대입 (Back Substitution)
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = mat[i][n]
        for j in range(i + 1, n):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]
    
    return [int(round(val)) for val in x]


def main():
    n = int(input())
    mat = [list(map(float, input().split())) for _ in range(n)]
    result = gaussian_elimination(mat, n)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
