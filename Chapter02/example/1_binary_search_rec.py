lst = [0, 1, 2, 4, 5, 7, 8, 10, 12, 13, 14, 16, 19, 20]
x = 7

def binary_search_rec(low, high):
    if low > high:
        return 0
    mid = (low + high) // 2
    if x == lst[mid]:
        return mid
    elif x < lst[mid]:
        return binary_search_rec(low, mid - 1)
    else:
        return binary_search_rec(mid + 1, high)

if __name__ == "__main__":
    print(binary_search_rec(0, len(lst) - 1))