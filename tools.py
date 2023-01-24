from time import time
import math


def timer_func(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f'Took {t2 - t1} seconds to run')
        return res
    return wrapper_func

def fibonacci_fi(n):
    fi = 0.5 * (1 + math.sqrt(5))
    psi = 0.5 * (1 - math.sqrt(5))
    return round((fi ** n - psi ** n) / math.sqrt(5))


def get_divisors(n):
    divisors = []
    for i in range(1, round(math.sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return divisors