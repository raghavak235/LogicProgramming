# Write a program to find column wise sum in the matrix.
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
# sum of each column
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 12
# 15
# 18

def column_wise_sum():
    #  For columns we're taking a[j[i]
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