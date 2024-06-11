# Rotate String
# Given two strings s and goal, return true if and only if s can become goal after
# some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost
# position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
# abcde
# bcdea
# cdeab
# deabc
# eabcd
# x and y
# abcde
# bcdea
# abcdeabcde
# bcdea


def rotate_string():
    s1= input()
    s2= input()
    if s2 in s1 + s2:
        print(True)
