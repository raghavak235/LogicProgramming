#
# Implement a program to sort the all the column values in desc order
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
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 7 8 9
# 4 5 6
# 1 2 3


def column_desc():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    a = [l1, l2, l3]
    ll = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            ll[i][j] = a[j][i]
    for i in range(3):
        ll[i].sort(reverse=True)
    for i in range(3):
        for j in range(3):
            print(ll[j][i], end=' ')
        print()