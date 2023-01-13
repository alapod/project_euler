from tools import fibonacci_fi


def thousand_digit_fibonacci():     #ran out of memory, noticed that the number of digits was ~ i/5
                                    #then guessed the exact number (4700th, 4800th, 4770th etc.) using wolphram
    n = 1000
    f = fibonacci_fi(n)
    while len(str(f)) < 1000:
        ...


for i in range(1, 1450):
    ith_fib_len = len(str(fibonacci_fi(i)))
    print(f'4.77 - i/len={4.782 - i / ith_fib_len}')


#ith_fib_len = 1000
#i?

#i/len~~4.7
#i=4.76*len
