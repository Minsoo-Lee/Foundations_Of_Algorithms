import random
lst = []
for _ in range(100):
    lst.append(random.randint(0, 500))

min = lst[0]
for i in range(1, 100):
    if min > lst[i]:
        min = lst[i]

print(min)