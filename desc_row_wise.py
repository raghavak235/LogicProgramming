# Implement a program to sort all the row wise elements in desc order
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
# 4 5 6
# 7 9 8
# Sample Output 0
#
# 3 2 1
# 6 5 4
# 9 8 7

def desc_row():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    a = [l1, l2, l3]
    ll = []
    for i in range(3):
        a[i].sort(reverse=True)
    for i in range(3):
        for j in range(3):
            print(a[i][j], end=' ')
        print()