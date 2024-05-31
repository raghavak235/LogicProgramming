# Check if String ending matches second String
# Problem Statement: Create a function/method that takes two Strings and
# returns true of the first string ends with second string, otherwise return false.
# Input: two strings
# Constraints: No
# Output: true or false

def string_ending():
    n1 = input()
    n2 = input()
    if n2.endswith(n1):
        print('True')
    print('False')
