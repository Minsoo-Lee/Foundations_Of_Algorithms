from operator import truediv


a, b = 30, 24
gcd = min(a, b)

while True:
    if a % gcd == 0 and b % gcd == 0:
        break
    gcd -= 1

print(gcd)