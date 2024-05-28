#
# Program to count number of special characters and white spaces in a given
# string.
# input --------> A string from the user
# constraint ---> non-empty string
# output -------> number of special characters

def special_characters():
    stri = input()
    ws=0
    for i in stri:
        if i.isspace():
            ws +=1

