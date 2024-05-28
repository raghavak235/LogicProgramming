# Implement a program to return First capital letter in a String
# input -------> A string from the user
# constraint --> non-empty string
# output ------> First Capital letter

def first_capital_string():
    s=input()
    for i in s:
        if i.isupper():
            print(i)
        break