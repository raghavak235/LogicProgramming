# LBP201

# Program to read matrix elements of order n x m and display on the console.
#
# Input Format
#
# A matrix of order n x m.
#
# Constraints
#
# 1<=n<=5
# 1<=m<=5
#
# Output Format
#
# Print the same matrix

# I/P:
# 2
# 2
# 1 2
# 3 4
def read_matrix():
    r = int(input())
    c = int(input())
    a = []
    for i in range(r):
        a.append([int(i) for i in input().split()])
    # print(a)
    for i in range(r):
        for j in range(c):
            print(a[i][j], end=' ')
        print()

read_matrix()