# You are given an array of integers, a of size n, Your task is to find the number of elements whose positions will remain unchanged after sorted in ascending order.
#
# Input Format
#
# array size and elements
#
# Constraints
#
# no
#
# Output Format
#
# unchanged count
#
# Sample Input 0
#
# 5
# 1 2 5 3 4
# Sample Output 0
#
# 2

def ele_pos_unchanged():
    n=5
    l=[1,2,5,3,4]
    l1=l.copy()
    l1.sort()
    c=0
    for i in range(n):
        if l[i]==l1[i]:
            c=c+1
