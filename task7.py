from math import log, sqrt, ceil


def estimate(n):
    return n * log(n) + n * log(log(n))


def find_primes(n):
    nums = [True] * (n+1)
    for i in range(2, round(sqrt(n))):
        if nums[i]:
            for j in range(i ** 2, n+1, i):
                nums[j] = False
    primes = [index for index, item in enumerate(nums) if item]
    return primes[2:]


if __name__ == "__main__":
    print(find_primes(ceil(estimate(10001)))[10000])