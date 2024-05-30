# Next Prime
# Given an integer,
# create a function that returns the next prime.
# If the number is prime, return the number itself.
# input ----------> a number
# constraint -----> prime number
# output ---------> prime number


def is_prime(n):
    f=0
    for i in range(1, n+1):
        if n%i ==0:
            f=f+1
    return f==2

def next_prime():
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            break
        n = n+1


next_prime()



