# sum of prime numbers in an array
# Implement a program to read an array elements and print sum of all prime
# elements
# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all prime elements


def isprime(n):
    f=0
    for i in (1,n+1):
        if n%i ==0:
            f=f+1
    return f==2

def sum_primes():
    l=[1,2,3,4,5]
    print(sum([i for i in l if isprime(i)]))
