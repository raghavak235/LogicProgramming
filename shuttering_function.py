# Stuttering Function
# write a function that shutters a word as if someone is struggling to read it.
# The first two letters are repeated twice with an ellipsis ... , and then the word is
# pronounced with a question mark?
# input ------------> a string
# contraint --------> no
# output -----------> xx...xx...~~~~~~~?

def shattering_string_functions():
    n,s = input()
    twochars= n[:3]+'...'
    print(twochars+twochars+n+'?')
    # OR
    print(f"{s[0]}{s[1]}...{s[0]}{s[1]}...{s}?")

shattering_string_functions()
