# Valid Hex Code
# Create a function that determines whether a string is a valid hex code.
# A hex code must begin with a pound key # and is exactly 6 characters in length.
# Each character must be a digit from 0-9 or an alphabetic character from A-F.
# All alphabetic characters may be uppercase or lowercase.
# input -----> a string from the user
# con -------> no
# output ----> true or false

def valid_hexa_code_verify():
    code = input()
    if not code.startswith('#') and len(code) !=6:
        print('false')
