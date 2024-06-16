# Write a program to find the digital root of a given number. Digital root is the recursive sum of digits in the given number (until single digit is arrived)
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
# single digit number
#
# Sample Input 0
#
# 2478
# Sample Output 0
#
# 3


def sum(n):
    sum=0
    while n!=0:
        digit = n%10
        sum = sum + digit
        n = n//10
    return sum
def digital_root():
    n=2478
    s=0
    while 0<= n <=9:
        print(n)
        break
    else:
       n = sum(n)


