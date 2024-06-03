# zipcodes consists of 5 consecutive digits.
# Given a string,
# write a function to determine whether the input is a valid zip code.
# a valid zipcode is as follows
# 1. must contain only numbers.
# 2. it should not contain any spaces.
# 3. length should be only 5.
# input ------> A string
# constraint -> no
# output -----> true or false

def zipcode_validation():
    zp = (input())
    if len(zp) == 5:
        print('not a valid zones')
        for i in zp:
            if not i.isspace() and i.isdigit():
                print('valid zipcode')
        print('not a valid zip code')