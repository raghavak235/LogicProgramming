# wo strings are said to the same if they are of the same length and have the same character at each index. Backspacing in a string removes the previous character in the string.
# Given two strings containing lowercase english letters and the character '#' which represents a backspace key. determine if the two final strings are equal or not. Return 1 if they are equal else 0.
#
# Input Format
#
# two strings s1 and s2
#
# Constraints
#
# no
#
# Output Format
#
# 1 or 0
#
# Sample Input 0
#
# axx#bb#c
# axbd#c#c
# Sample Output 0
#
# 1
#

def backspace_strings():
    n1= 'axx#bb#c'
    n2= 'axbd#c#c'
    s3=[]
    s4=[]

    for i in range(len(n1)-1):
        if n1[i+1] !='#'and n1[i]!='#':
            print(n1[i], end=' ')

    for i in range(len(n2)-1):
        if n2[i+1] !='#'and n2[i]!='#':
            print(n2[i], end=' ')

    print(True if s3==s4 else False)



backspace_strings()
