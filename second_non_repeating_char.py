# sofia loved to play with the programs unfortunately. she got stuck in one of the questions.
# she tought to take help of james. james asked her the problem statement. The problem statement was.
# "for the given string S of length N consist of stream of character not in predefined order.
# Write a program to find second non-repeating character in a string S. Write a program to help sofia and james for the given problem statements.
#
# Input Format
#
# string from the user
#
# Constraints
#
# no
#
# Output Format
#
# single character
#
# Sample Input 0
#
# gaahaajapsps
# Sample Output 0
#

def sec_non_repeating_prog():
    s='gaahaajapsps'
    l=[]
    for i in s:
        if s.count(i)==1:
            l.append(i)

    print(l[1])