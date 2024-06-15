# Program to read matrix elements and find sum of all elements in the matrix.
#
# Input Format
#
# A matrix of order n x m.
#
# Constraints
#
# 1<=n<=5
# 1<=m<=5
#
# Output Format
#
# Print sum of matrix elements
#
# Sample Input 0
# 2
# 2
# 1 2
# 3 4

def sum_ele_matrices():
    r = int(input())
    c = int(input())
    a = []
    sum = 0
    for i in range(r):
        a.append([int(i) for i in input().split()])
    for i in range(r):
        for j in range(c):
            sum += a[i][j]
    print(sum)