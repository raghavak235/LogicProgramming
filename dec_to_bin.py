# Decimal to Binary
# A network protocol specifies how data is exchanged via transmission media.
# The protocol converts each message into a stream of 1's and 0's.
# Given a decimal number, write an algorithm to convert the number into a
# binary form.
# input ---------> a number
# constraint ----> n>=0
# output --------> binary number


#  Base Decimal - 10
#  Base Binary - 2

# bin in python always have ob before output. 0b1111011

# In order to remove it use [2:]
def dec_to_bin():
    dec = int(input())
    print(bin(dec)[2:])

dec_to_bin()