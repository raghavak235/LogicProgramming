# Returns the middle character of a string
# create a function that takes a string and returns, the middle character(s).
# if the word's length is odd return the middle character.
# if the word's length is even, return the middle two characters.
# input -----> a string from the user
# constraint-> no
# output ----> middle character(s)

def middle_characters():
    string =input()
    len_str = len(string)//2
    if len(string)%2!=0:
        print(string[len_str])
    else:
        print(string[len_str-1], string[len_str],sep='')