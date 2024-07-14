# The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

def fibonacci(n):
    if n==0:
        return 0

    # we are verifying the 1st and 2nd term
    elif n in [1,2]:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

