# C*ns*r*d Str*ngs
# Someone has attempted to censor my strings by replacing every vowel with a
# *, l*k* th*s.
# Luckily, I've been able to find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the original
# uncensored string.
# input --------> original & replacement strings
# con ----------> no
# output -------> updated string after replacement

def censor_string_replacement():
    cs= input()
    w = input()
    j=0
    for i in cs:
        if i == '*':
            print(w[j],end='')
            j=j+1
        else:
            print(i,end='')