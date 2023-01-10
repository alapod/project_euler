from tools import timer_func


def get_next(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def get_collatz_chain(n):
    i = get_next(n)
    res = 2
    while i != 1:
        i = get_next(i)
        res += 1
    return res


@timer_func
def get_longest_collatz():
    max_len = 0
    res = 1
    for i in range(1, 1000000):
        curr = get_collatz_chain(i)
        if curr > max_len:
            res = i
            max_len = curr
    return res
