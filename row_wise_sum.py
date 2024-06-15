# Write a program to find row wise sum in the matrix.
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
# sum of each row
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9

def row_wise_sum():
    r = 3
    c = 3
    a = []

    for i in range(r):
        a.append([int(i) for i in input().split()])
    for i in range(r):
        sum = 0
        for j in range(c):
            sum += a[i][j]
        print(sum)