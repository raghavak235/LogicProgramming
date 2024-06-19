# Write a program to perform multiplication operation on two matrices
#
# Input Format
#
# two 3x3 matrices
#
# Constraints
#
# no
#
# Output Format
#
# resultent matrix
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# 1 0 0
# 0 1 0
# 0 0 1
# Sample Output 0
#
# 1 2 3
# 4 5 6
# 7 8 9

def multiplication_matrices():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    a = [l1, l2, l3]

    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    b = [l1, l2, l3]
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            c[i][j] = 0
            for k in range(3):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    for i in range(3):
        for j in range(3):
            print(c[i][j], end=' ')
        print()