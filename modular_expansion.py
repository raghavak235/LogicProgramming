# Given three numbers b,e, and m. fill in a function that takes these three positive integer values and outputs b^e mod m.
#
# Input Format
#
# b,e and m values
#
# Constraints
#
# no
#
# Output Format
#
# b^e mod m
#
# Sample Input 0
#
# 2 1 2
# Sample Output 0
#
# 0

def modular_imp():

    b,e,m=(int(i) for i in input().split())
    print(b**e%m)