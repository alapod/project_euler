from math import sqrt


def check_ab(lim=500**2):
    squares = [i for i in range(2, lim) if int(sqrt(i)) == sqrt(i)]
    for i in range(len(squares)):
        for j in range(i, len(squares)):
            if squares[i] + squares[j] in squares:
                if sqrt(squares[i]) + sqrt(squares[j]) + sqrt(squares[i] + squares[j]) == 1000:
                    return sqrt(squares[i]) * sqrt(squares[j]) * sqrt(squares[i] + squares[j])



