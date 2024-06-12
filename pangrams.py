# Pangrams
# Implement a program to check whether the given string pangram or not.
# A pangram is a string that contains all the letters of the English alphabet.
# An example of a pangram is "The quick brown fox jumps over the lazy dog"
# input ----> a string from the user
# con ------> non-empty string
# output ---> Yes or No

def pangrams_checking():
    m = input()
    ss='abcdefghijklnopqrstuvwxyz'
    flag=True
    for i in ss:
        if i not in m:
            flag = False
