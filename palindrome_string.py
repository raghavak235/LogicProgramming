# Valid Palindrome
# Given a string,
# determine if it is a Palindrome string or not.
# A String is Palindrome if it is equal to reverse of the original string.
# input ------> A String from the user
# constriant--> Non-empty String
# output -----> Palindrome or not

def palindrome_string():
    s = input()
    print("valid" if s == s[::-1] else "invalid")
    pass
