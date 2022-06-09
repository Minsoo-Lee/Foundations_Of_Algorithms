import random

def sum_lst(lst):
    sum = 0
    for index in lst:
        sum += index
    return sum

if __name__ == "__main__":
    lst = []
    for _ in range(10):
        lst.append(random.randint(0, 20))
    print(lst)
    print(sum_lst(lst))