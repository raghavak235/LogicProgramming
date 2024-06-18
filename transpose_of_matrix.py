# Implement a program to print transpose of a matrix
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
# print transpose of the matrix
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 1 4 7
# 2 5 8
# 3 6 9

def transpose_matrix():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    l = [l1, l2, l3]
    for i in range(3):
        for j in range(3):
            print(l[j][i], end=' ')
        print()