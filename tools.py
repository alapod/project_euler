from time import time


def timer_func(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f'Took {t2 - t1} seconds to run')
        return res
    return wrapper_func