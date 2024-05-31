# Space between each character
# Create a function that takes a string and returns a string with spaces in
# between all of the characters.
# input ------------> a string
# constraints-------> No
# output -----------> string

def char_sting_space():
    s = input()
    for i in s:
        print(i, end=' ')
    print(' '.join([i for i in input()]))