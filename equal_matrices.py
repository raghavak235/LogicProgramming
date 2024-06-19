# Implement a program to check whether the given matrices are equal or not
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
# Yes or No
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# Yes

def comparing_matrices():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    a = [l1, l2, l3]

    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    b = [l1, l2, l3]
    flag = True
    for i in range(3):
        for j in range(3):
            if a[i][j] != b[i][j]:
                flag = False
                break

    print('Yes' if flag == True else "No")