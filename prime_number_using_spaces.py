# Implement a program to read a number and print prime numbers upto n seperated by spaces.
#
# Input Format
#
# a number from the user
#
# Constraints
#
# no
#
# Output Format
#
# space seperated prime numbers
#

def is_prime(n):
    f=0
    for i in range(1, n+1):
        if n%i ==0:
            f=f+1
    return f==2



def print_prime_numbers():
    n=10
    for i in range(2, n+1):
        if is_prime(i):
            print(i, end=' ')

print_prime_numbers()