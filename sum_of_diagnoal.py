# Write a program to find sum of diagonal elements in matrix.
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
# sum of diagonal elements
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 15

def sum_of_diagonal():
    # For diagonal, rows and columns will be the same. i and i
    r = 3
    c = 3
    a = []
    sum = 0
    for i in range(r):
        a.append([int(i) for i in input().split()])
    for i in range(r):
        for j in range(c):
            if i==j:
                sum += a[i][j]
    print(sum)