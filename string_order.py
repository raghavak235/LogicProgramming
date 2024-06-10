# Is the String in Order?
# Create a function that takes a string and returns true or false,
# depending on whether the characters are in order or not.
# input -------> a string from the user
# cons --------> for non-empty string print invalid
# output ------> true or false

def string_order():
    n = input()
    list(n).sort()
    out = ''.join(n)
    print(out == n)
