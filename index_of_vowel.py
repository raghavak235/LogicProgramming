# Index of first vowel
# create a function that returns the index of first vowel in a string
# input ------> a string
# con --------> no
# output -----> an int value

def index_str_vowel():
    n  =input()
    vw ='aeiou'
    for v in vw:
        if v in n:
            print(n.index(v))
            break

index_str_vowel()