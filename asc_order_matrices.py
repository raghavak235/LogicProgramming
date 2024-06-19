# Implement a program to sort all the elements in asc order in the matrix
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
# 1 3 2
# 6 7 9
# 5 4 8
# Sample Output 0
#
# 1 2 3
# 4 5 6
# 7 8 9

def asc_order_matrix():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    a = [l1, l2, l3]
    ll = []

    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            ll.append(a[i][j])
    ll.sort()

    k = 0
    for i in range(3):
        for j in range(3):
            c[i][j] = ll[k]
            k = k + 1
    for i in range(3):
        for j in range(3):
            print(c[i][j], end=' ')
        print()


