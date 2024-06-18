# Implement a program to check whether the given matrix is identity matrix or not
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
# 1 0 0
# 0 1 0
# 0 0 1
# Sample Output 0
#
# Yes

def identity_matrix():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    es = 0
    os = 0
    l = [l1, l2, l3]
    flag = True
    for i in range(3):
        for j in range(3):
            if i == j and l[i][j] != 1:
                flag = False
                break
            elif i != j and l[i][j] != 0:
                flag = False
                break

    print('Yes' if flag == True else "No")