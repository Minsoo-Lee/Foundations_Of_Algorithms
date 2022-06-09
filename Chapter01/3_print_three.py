import random
lst = []
for _ in range(10):
    lst.append(random.randint(0, 500))
one = 0
two = 1
three = 2

while one < len(lst) - 2:
    print(lst[one], lst[two], lst[three])
    if two == len(lst) - 2:
        one += 1
        two = one + 1
        three = two
    if three == len(lst) - 1:
        two += 1
        three = two
    three += 1
