def multi_matrix(a, b, c):
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                c[i][j] = a[i][k] * b[k][j]

if __name__ == "__main__":
    a = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    b = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    multi_matrix(a, b, c)
    print(c)