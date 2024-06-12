# Replace character with it's occurrence
# Implement a Program to replace a character with it's occurrence in given
# string.
# input ---------> a string and a character from the user.
# con -----------> non-empty string
# output --------> replaced stringx
def replace_char():
    n  = input()
    rep_char = input()
    c = 1
    output_str = ''
    for i in n:
        if i==rep_char:
            output_str += str(c)
            c=int(c+1)  
        else:
            output_str += i
    print(output_str)
replace_char()