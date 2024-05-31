# Repeating Letters
# Create a method that takes a string and returns a string in which each
# character is repeated once.
# input ---------------> String from the user
# constraint ----------> No
# output --------------> String

def repeat_string_chars():
    s = input()
    for i in s:
        print(i * 2, end='')