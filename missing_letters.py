# Missing Letters
# Given a string containing unique letters, return a sorted string with the letters
# that don't appear in the string.
# input ---------> a string from the user
# con -----------> no
# output --------> return missing characters

# The ord() function converts a character into its Unicode point,
# while chr() does the opposite, converting a Unicode point back into its corresponding character.
# Chr(65)	A
# Chr(90)	Z
# Chr(97)	a
# Chr(122)  z


def missing_letter():
    n = input()
    for i in range(97,123):
        if chr(i) not in n:
            print(chr(i), end='')