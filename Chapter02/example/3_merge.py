def merge(h, m, u, v, s):
    i, j, k = 1, 1, 1
    while i < h and j < m:
        if u[i] < v[j]:
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1
        k += 1
    if i > h:
        for index in range(j, m):
            s[index + i] = v[index]
    else:
        for index in range(i, h):
            s[index + i] = u[index]