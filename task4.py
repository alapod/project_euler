import math


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def find_largest_palindrome():
    palindromes = []
    for i in range(999, 100, -1):
       # print(i)
        for j in range(i, 100, -1):
         #   print(i, j)
            if is_palindrome(i * j):
                palindromes.append(i * j)
    return sorted(palindromes)[-1]

