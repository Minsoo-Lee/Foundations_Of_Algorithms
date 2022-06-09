def fib(n):
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[n]

if __name__ == "__main__":
    for i in range(0, 10):
        print(fib(i), end = " ")
