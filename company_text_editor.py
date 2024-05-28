# A company launched a new text editor that allows users to enter english
# letters, numbers and white spaces only.
# If a user attempts to enter any other type of characters, it is counted as miss.
# Given a String text,
# write an algorithm to help the developer detect the number of misses by a
# given user in the given input.
# input --------> String
# constraint ---> non-empty string
# output -------> number of misses

def non_empty_strings():
    s = input()
    c = 0
    for i in s:
        if i.isalnum() or i.isspace():
            continue
        else:
            c = c + 1
    print(c)