# Replace Letters With Position In Alphabet
# Create a function that takes a string and replaces each letter with its
# appropriate position in the alphabet.
# "a" is 1, "b" is 2, "c" is 3, etc, etc.
# Note: If any character in the string isn't a letter, ignore it.
# input -----------> a string from the user
# constriant ------> non-empty string
# output ----------> position of characters seperated by space

def replace_letter():
    # For
    # s[0] = 'a': ord('a') - 96 is 1, so
    # 1 is printed.
    # For
    # s[1] = 'b': ord('b') - 96 is 2, so
    # 2 is printed.
    # For
    # s[2] = 'c': ord('c') - 96 is 3, so
    # 3 is printed.
    n = input()
    for i in n:
        if 'a'<=i<='z':
            print(ord(i)-96, end = ' ')

replace_letter()