import math


def factorize(n):
    factors = []
    k = 2
    l = n
    while k <= math.sqrt(n):
        if l % k == 0:
            factors.append(k)
            l = l / k
            k += 1
        else:
            k += 1
    return factors + [n // x for x in factors]


def is_prime(n):        # for readability
    return not factorize(n)


def find_prime_factors(n):
    factors = factorize(n)
    prime_factors = sorted((x for x in factors if is_prime(x)))
    return prime_factors[-1]

