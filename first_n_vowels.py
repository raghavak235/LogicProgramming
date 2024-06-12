# First N Vowels
# Write a function that returns the first n vowels of a string.
# input ------> a string from the user and an integer value
# cons -------> Return "invalid" if the n exceeds the number of vowels in a string.
# output -----> return first n vowels in the string

def first_n_vowels():
    word = input()
    num = int(input())
    count=0
    vow = 'aeiou'
    new_str=''
