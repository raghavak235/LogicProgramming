# Michael wants to check the parity of the given number. To find tha parity, follow below steps.
# 1. convert decimal number into binary number.
# 2. count the number of 1's and 0's in the binary representation.
#
# if it contains odd number of 1-bits, then it is "odd parity" and
# if contains even number of 1-bits then "even parity"
# Write a program to validate the given number belongs to odd parity or even parity.
#
# Input Format
#
# a number from the user.
#
# Constraints
#
# no
#
# Output Format
#
# odd parity or even parity.

def parity_bits():
    n = 5
    n_bin = bin(n) #Convert to binary
    if n_bin[2:].count('1')%2==0:
        print('EVEN')
    else:
        print('ODD')

parity_bits()