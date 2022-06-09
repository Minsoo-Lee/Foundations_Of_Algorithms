def binary_search(lst, x):
    low, high = 1, len(lst) - 1
    index = -1
    while low <= high and index == 0:
        mid = (low + high) // 2
        if x == lst[mid]:
            index = mid
        elif x < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return index

if __name__ == "__main__":
    lst = [0, 1, 2, 4, 5, 7, 8, 10, 12, 13, 14, 16, 19, 20]
    print(binary_search(lst, 4))