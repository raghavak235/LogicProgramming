# Number of vowels
# Implement a program to return number of vowels present in the given string
# input ---------> a string from the user
# con -----------> non-empty string
# output --------> return number of vowels

def count_vowel():
    n = input()
    vs='aeiou'
    vc=0
    for i in vs:
        if i in n:
            vc +=1
    print(vc)
