# Given a maximum of 100-digit numbers as input, find the difference between the sum of odd and even position digits.
#
# Input Format
#
# a number from the user
#
# Constraints
#
# no
#
# Output Format
#
# an integer
#

def odd_even_position():
    n='45712'
    dict={}
    os,es=0,0
    for i in range(len(n)):
            dict[i]=n[i]
    print(dict)
    for k in dict.keys():
        if k%2==0:
            es = es + int(dict.get(k))
        else:
            os = os + int(dict.get(k))
    print(es-os)
odd_even_position()

