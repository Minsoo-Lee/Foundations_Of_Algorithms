def bin(n, k):
    B = [[0 for x in range(0, n + 1)] for x in range(0, k + 1)]
    for i in range(0, n + 1):
        for j in range(0, min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    for i in range(0, n):
        for j in range(0, k):
            print(B[i][j], end = " ")
        print()
    return B[n][k]

bin(5, 5)