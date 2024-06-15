# Write a program to find sum of all prime elements in the matrix.
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
# sum of all prime elements
#
# Sample Input 0
#
# 1 2 3
# 4 5 6
# 7 8 9

def isprime(n):
    f=0
    for i in range(1,n+1):
        if n % i ==0:
            f=f+1
    return f==2
def prime_numbers_matrix():
    r = 3
    c = 3
    a = []
    sum = 0
    for i in range(r):
        a.append([int(i) for i in input().split()])
    for i in range(r):
        for j in range(c):
            if isprime(a[i][j]):
                sum += a[i][j]
    print(sum)