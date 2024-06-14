# All Numbers In Array Are Prime
# Create a function thats takes an array of integers and returns true if every
# number is prime.
# Otherwise, return false.
# input -------> size and an array
# con ---------> 1 is not a prime number.
# output ------> true or false


def isprime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f=f+1
    return f==2

def primes():
    L=[2,3,5]
    n=3
    c=0
    for i in L:
         if isprime(i):
                c=c+1
    print(c)
    print("true" if c==n else "false")

primes()