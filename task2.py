"""
Fn = Fn-1 + Fn-2
   = Fn-2 + Fn-3 + Fn-3 + Fn-4
   = Fn-2 + 2Fn-3 + Fn-4
   = Fn-3 + Fn-4 + 2Fn-3 + Fn-4
   = 3Fn-3 + 2Fn-4
   = 3Fn-3 + Fn-4 + Fn-5 + Fn-6
   = 4Fn-3 + Fn-6

Every 3rd item is even.

EFx = 4EFx-1 + EFx-2
"""


def fibonacci(n):
    if n in (0, 1):
        return n + 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def even_fibonacci(n):
    base = [2, 8]
    if n in (0, 1):
        return base[n]
    return 4 * even_fibonacci(n - 1) + even_fibonacci(n - 2)


def sum_even_fibonacci(limit):
    result = 0
    i = 0
    n = even_fibonacci(i)
    while n <= limit:
        print(i, n)
        result += n
        i += 1
        n = even_fibonacci(i)
    return result





