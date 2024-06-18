# Write a program to find frequency of odd and even elements in the matrix excluding 0.
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
# odd elements and even elements count
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 0
#
# 5
# 4

def freq_even_odd():
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [int(i) for i in input().split()]
    es = 0
    os = 0
    l = [l1, l2, l3]
    for i in range(3):
        for j in range(3):
            if l[i][j] % 2 == 0 and l[i][j] != 0:
                es += 1
            elif l[i][j] % 2 != 0 and l[i][j] != 0:
                os += 1
    print(os)
    print(es)