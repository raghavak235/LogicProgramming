# American keyboard
# Given a string, return the true if that can be typed using letters of alphabet on
# only
# one row's of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
# dad ---> true
# mom ---> false
# Note:
# 1. You may use one character in the keyboard more than once.
# 2. You may assume the input string will only contain letters of alphabet.
# input -------> a string from the user
# cons -------> no
# output ------> true or false

def string_keyboard():
    n = input()
    c1,c2,c3=0,0,0
    for i in n:
        if i in "qwertyuiop":
            c1 += 1
        elif i in 'asdfghjkl':
            c2 +=1
        elif i in 'zxcvbnm':
            c3 +=1
    print(True if (c1==len(n) or c2 ==len(n) or c3 ==len(n))else False)