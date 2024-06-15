# Implement a program to read two integer values and return GCD of two numbers.
#
# Input Format
# two space separated integers.
# Constraints
# no
# Output Format
# GCD of two numbers(common factors)

def GCD_of_numbers():
    a=98
    b=56

    while b>0:
        r= a%b
        a=b
        b=r
    print(a)
GCD_of_numbers()