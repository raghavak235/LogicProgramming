# Duck Number
# Program to read a number and check whether it is duck number or not.
# Hint: A duck number is a number which has zeros present in it,
# but no zero present in the begining of the number.
# If any number begin with 0 then it is said to be octal.
# input-------> a number from the user
# contraint --> n>=0
# output------> Yes or No

def duck_number():
    n = (input())
    if '0' in n and int(n[0]) != 0:
        print('Yes')
    else:
        print('No')

duck_number()