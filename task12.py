from math import sqrt


def get_triangle_number(n):
    return n * (1 + n) / 2


def get_divisors_number(n):
    divisors = []
    for i in range(1, round(sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return len(divisors)


def get_highly_divisible():
    curr = 1
    i = 1
    while curr < 500:
        curr = get_divisors_number(get_triangle_number(i))
        i += 1
        if i % 1000 == 0:
            print(i)
    return get_triangle_number(i - 1)

