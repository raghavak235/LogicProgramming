# Number of consonants
# Implement a program to return number of consonants present in the given
# string
# input ---------> a string from the user
# con -----------> non-empty string
# output --------> return number of consonants

def count_consonant():
    n =input()
    ss='aeiou'
    c=0
    for i in ss:
        if i not in n:
            c+=1