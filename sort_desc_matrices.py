# Implement a program to sort all the elements in desc in the matrix
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
# 9 8 7
# 6 5 4
# 3 2 1


def desc_matrix():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    a = [l1, l2, l3]
    ll = []

    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            ll.append(a[i][j])
    ll.sort(reverse=True)

    k = 0
    for i in range(3):
        for j in range(3):
            c[i][j] = ll[k]
            k = k + 1
    for i in range(3):
        for j in range(3):
            print(c[i][j], end=' ')
        print()
