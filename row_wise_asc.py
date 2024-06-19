# Implement a program to sort all the rowwise elements in asc order
#
# Input Format
#
# a matrix
#
# Constraints
#
# no
#
# Output Format
#
# result matrix
#
# Sample Input 0
#
# 3 2 1
# 4 6 5
# 9 7 8
# Sample Output 0
#
# 1 2 3
# 4 5 6
# 7 8 9

def row_wise_asc():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    a = [l1, l2, l3]
    ll = []
    for i in range(3):
        a[i].sort()
    for i in range(3):
        for j in range(3):
            print(a[i][j], end=' ')
        print()