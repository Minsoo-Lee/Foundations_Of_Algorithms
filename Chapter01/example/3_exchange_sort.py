import random

def exchange_sort(lst):
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst) - 1):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]

if __name__ == "__main__":
    lst = []
    for _ in range(10):
        lst.append(random.randint(0, 20))
    print(lst)
    exchange_sort(lst)
    print(lst)
