def find_missing(n, nums):
    for i in nums:
        if n % i == 0:
            return i
    return n


def get_evenly_divisible(limit):
    nums = [2]
    curr = nums[0]
    for i in range(3, limit):
        if curr % i == 0:
            continue
        else:
            num = find_missing(i, nums)
            curr *= num
            nums.append(num)
    return curr

