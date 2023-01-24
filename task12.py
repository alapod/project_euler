from tools import get_divisors


def get_triangle_number(n):
    return n * (1 + n) / 2


def get_divisors_number(n):
    return len(get_divisors(n))


def get_highly_divisible():
    curr = 1
    i = 1
    while curr < 500:
        curr = get_divisors_number(get_triangle_number(i))
        i += 1
        if i % 1000 == 0:
            print(i)
    return get_triangle_number(i - 1)

