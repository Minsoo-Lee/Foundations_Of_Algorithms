# 이항계수(binomial coefficient) : n개의 물체에서 한 번에 k개를 뽑는 조합의 수를 구하는 식
#                                (a^k)(b^(n-k))의 계수

def bin(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bin(n - 1, k - 1) + bin(n - 1, k)
