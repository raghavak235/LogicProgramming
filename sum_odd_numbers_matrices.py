# Write a program to find sum of all odd elements in the matrix.
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
# sum of all odd elements
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9

def sum_of_odd_ele_matrix():
    r = 3
    c = 3
    a = []
    sum = 0
    for i in range(r):
        a.append([int(i) for i in input().split()])
    for i in range(r):
        for j in range(c):
            if a[i][j] % 2 != 0:
                sum += a[i][j]
    print(sum)