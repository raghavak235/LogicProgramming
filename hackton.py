# Cristina appeared for a corporate Hackathon.
# She cleated first round of this and would like to take next challenge which is coding round.
# The problem statement comes to her is
# "Write a program to find numbers which are in between integer 2 and integer N and such that the sum of its digits raised to the third power is equal to the number with the input given.
#
# Input Format
#
# integer N
#
# Constraints
#
# no
#
# Output Format
#
# an integer value
#
# Sample Input 0
#
# 200
# Sample Output 0
#
# 153

def sum(n):
    s=0
    while n!=0:
        digit = n%10
        s = s + (digit*digit*digit)
        n =n//10
    return s



def amstrong_number():
    n=200
    # prob statement ask to take it from 2
    for i in range(2, n+1):
        if i ==sum(i):
            print(i)




