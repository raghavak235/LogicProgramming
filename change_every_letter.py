# Change Every Letter to the Next Letter
# Write a function that changes every letter to the next letter:



# The expression chr(ord(char) + 1) is used to get the next character in the ASCII/Unicode sequence. Here's a detailed explanation of how it works:
#
# ord(char):
#
# The ord() function takes a single character and returns its corresponding ASCII/Unicode code point. For example, ord('a') returns 97.
# ord(char) + 1:
#
# This increments the code point of the character by 1. For example, if char is 'a', then ord('a') + 1 results in 98.
# chr(ord(char) + 1):
#
# The chr() function takes an integer (ASCII/Unicode code point) and returns its corresponding character. For example, chr(98) returns 'b'.
# Thus, chr(ord(char) + 1) converts a character to its next character in the ASCII/Unicode sequence.
def change_every_letter():
    w = input()
    asci_val= ord(w)
    next_asci_val=ord(w)+1
    print(chr(ord(w)+1))