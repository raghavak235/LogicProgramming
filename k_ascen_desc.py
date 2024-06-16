# You are given a list of integers of size N, write an algorithm to sort the first K elements of the list in ascending order and the remaining elements in descending order.
#
# Input Format
#
# an array size and elements
#
# Constraints
#
# no
#
# Output Format
#
# updated array
#
# Sample Input 0
#
# 5
# 1 2 3 4 5
# Sample Output 0
#
# 1 2 5 4 3


def kth_asc_desc():
    b =5
    l = [1, 2, 3, 4,5]
    l.sort()
    length = b//2
    print(l[0:length],end=' ')
    print(l[length:][::-1])

kth_asc_desc()