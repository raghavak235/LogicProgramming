# VOWEL REPLACER
# Create a function that replaces all the vowels in a string with a specified
# character,
# input -----------> A string from the user and a character
# cons ------------> no
# output ----------> A string

def vowel_replacer():
    string = input()
    character = input()
    v ='aeiou'
    for i in v:
        string = string.replace(i, character)
    print(string)

vowel_replacer()