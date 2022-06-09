import random
lst = []
for _ in range(100):
    lst.append(random.randint(0, 500))

max = lst[0]
for i in range(1, 100):
    if max < lst[i]:
        max = lst[i]

print(max)