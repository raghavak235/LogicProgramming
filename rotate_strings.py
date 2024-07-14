# The problem is to rotate the string by k steps.
#
# This video will tell you how to take both the string and the number of characters by which you want to rotate the string as input from the console and then perform the left as well as the right rotation by that number of characters.


def rotate_strings_byk(string, n):

    #python -> py thon -> thonpy
    left_first = string[0:n]
    left_remaining= string[n:]
    print(left_remaining+left_first)

    # python -> pyth on -> onpytho
    right_remains=string[-n:]
    right_first = string[0:-n]

    print(right_remains+right_first)