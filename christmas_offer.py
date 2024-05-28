# Christmas offer
# An e-commerce company plans to give their customers a special discount for
# the Christmas,
# they are planning to offer a flat discount.
# The discount value is calculated as the sum of all prime digits in the total bill
# amount.
# Write an algorithm to find the discount value for the given total bill amount.
# input ----> the input consists of an integer order value representing the total
# bill amount
# condition-> no conditions
# output ---> print an integer representing discount value for the given total bill
# amount.

def christmas_offer():
    bill = input('Enter the bill amount')
    discount = sum([int(i) for i in bill if i in '2,3,5,7'])
    print(discount)


    pass

christmas_offer()