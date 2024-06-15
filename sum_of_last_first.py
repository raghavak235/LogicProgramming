# Write a program to find sum of first and last element in a matrix.
#
# Input Format
#
# a 3x3 matrix
#
# Constraints
#
# no
#
# Output Format
#
# sum of first and last element in matrix
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9

def first_last_diag():
    r = 3
    c = 3
    a = []
    sum = 0
    for i in range(r):
        a.append([int(i) for i in input().split()])

    print(a[0][0]+a[2][2])