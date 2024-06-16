# Write an algorithm to generate the token number from the application ID by doing this modifications.
# R1. If the digit is even add 1 to it.
# R2. If the digit is odd sub 1 from it.
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
# token number
#
# Sample Input 0
#
# 2347
# Sample Output 0
#
# 3256

def token_number():
    n='2347'[::-1]
    n_int= int(n)
    while n_int!=0:
        d=n%10
        if d%2==0:
            print(d+1)
        else:
            print(d-1)
        n=n//10
