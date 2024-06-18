# Implement a program to find trace(sum of diagonal elements) of the given matrix.
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
# print trace of the matrix
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 15

def diag_sum():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    l = [l1, l2, l3]
    s = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                s = s + l[i][j]
    print(s)