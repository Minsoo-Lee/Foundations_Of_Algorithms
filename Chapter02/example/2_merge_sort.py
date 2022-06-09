# ? again

# 3_merge.py
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
# 3_merge.py

def merge_sort(n, lst):
    if n > 1:
        h = n // 2
        m = n - h
        u = [0 for _ in range(0, h)]
        v = [0 for _ in range(h, n)]
        for index in range(0, h):
            u[index] = lst[index]
        for index in range(h, n):
            v[index - h] = lst[index]
        merge_sort(h, u)
        merge_sort(m, v)
        merge(h, m, u, v, lst)

if __name__ == "__main__":
    lst = [3, 6, 2, 1, 9, 7, 4, 8, 0, 5]
    merge_sort(len(lst), lst)
    print(lst)