from tools import get_divisors


def get_dn(n):
    return sum(get_divisors(n)) - n


def get_amicable_numbers(n):
    amicable = []
    for i in range(3, n):
        if i not in amicable:
            dn_i = get_dn(i)
            if get_dn(dn_i) == i and dn_i != i:
                amicable.append(i)
                amicable.append(dn_i)
    return sum(amicable)

