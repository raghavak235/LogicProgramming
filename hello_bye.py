# Say "Hello" Say "Bye"
# Write a function that takes a string name and number num (either 1 or 0) and
# return "Hello"+name if number is 1, otherwise "Bye"+name.
# input ------> a string from the user
# constraint -> no
# output -----> a string

def display():
    name= input()
    num=int(input())
    if 1 == num:
        print('Hello {}'.format(name))
    else:
        print('Bye {}'.format(name))