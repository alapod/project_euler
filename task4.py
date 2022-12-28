def is_palindrome(n):
    return str(n) == str(n)[::-1]


def find_largest_palindrome():
    palindromes = []
    for i in range(100, 999):
        for j in range(i, 999):
            if is_palindrome(i * j):
                palindromes.append(i * j)
    return sorted(palindromes)[-1]

