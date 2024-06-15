# One programming language has the following keywords that cannot be used as identifiers.
# break,case,continue,default,defer,else,for,func,goto,if,map,range,return,struct,type,var
# write a program to find if the given word is a keyword or not.
#
# Input Format
#
# string from the user
#
# Constraints
#
# con
#
# Output Format
#
# true or false
#
# Sample Input 0

def identifier():
    n='defer'
    string='break,case,continue,default,defer,else,for,func,goto,if,map,range,return,struct,type,var'
    if n in string:
        print(True)