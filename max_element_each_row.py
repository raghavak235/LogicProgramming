# Implement a program to print max element in each row of a matrix
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
# print max element in each row of a matrix
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 3
# 6
# 9

def max_each_row():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    l = [l1, l2, l3]
    print(max(l1))
    print(max(l2))
    print(max(l3))