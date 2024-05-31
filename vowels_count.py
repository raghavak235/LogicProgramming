# How many vowels
# Create a function that takes a string and returns the number of vowels
# contained within it.
# input -----------> a string
# constraint ------> no
# output ----------> number of vowels

def count_vowels():
    n =input()
    vow='aeiou'
    c=0
    for i in n:
        if i in n:
            c += 1