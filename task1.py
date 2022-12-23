def find_sum(first, second, limit, inclusive=False):
    if not inclusive:
        limit -= 1
    multiples_first = sum(first * x for x in range(limit // first + 1))
    multiples_second = sum(second * x for x in range(limit // second + 1))
    multiples_both = sum(first * second * x for x in range(limit // (first * second) + 1))
    return multiples_first + multiples_second - multiples_both
