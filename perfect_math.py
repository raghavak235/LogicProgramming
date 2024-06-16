# Perfect math is an online math program. In once of the assignments the system displays a list of N number and a value K, and students need to calculate the sum of remainders after dividing all the numbers from the list of N numbers by K. The system need to develop a program to calcualte the correct answer for the assignment.
# Write an algorithm to calcualte the correct answer for the assignment.
#
# Input Format
#
# size N and N elements and K value
#
# Constraints
#
# no
#
# Output Format
#
# an int value
#
# Sample Input 0
#
# 5
# 1 2 3 4 5
# 3
# Sample Output 0
#
# 6


def perfect_math():
    n=[1,2,3,4,5]
    c=3
    s=0
    for i in n:
        s= s+(i%c)