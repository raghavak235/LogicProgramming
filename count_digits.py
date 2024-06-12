# Implement a program to check if a string contains only digits.
# input ----> a string from the user
# con ------> no
# output ---> Yes or No
def count_digit():
    n = input()
    for i in n:
        if not i.isdigit():
            print(False)
            break