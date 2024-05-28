# Niven Number
# Write a program to accept a number and check and display whether it is a
# Niven Number or not.
# Niven Number is that a number which is divisible by its sum of digits.
# input -----> a number
# constraint-> n>0
# output ----> Niven Number or Not

def niven_number():
    n =  (input())
    sum_val = sum([int(i) for i in n])
    if int(n)%sum_val ==0:
        print('Niven')
    else:
        print('Not Niven')



niven_number()