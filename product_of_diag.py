#
# Write a program to find the product of diagonal matrix.
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
# find the product of diagonal matrix
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 45
#
#
#
def sum_even_matrices():
    r = 3
    c = 3
    a = []
    sum = 1
    for i in range(r):
        a.append([int(i) for i in input().split()])
    for i in range(r):
        for j in range(c):
            if i ==j:
                sum *= a[i][j]
    print(sum)