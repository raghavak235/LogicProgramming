# An e-commerce company plans to give their customers a discount for the
# new years holiday.
# The discount will be calculated on the basis of the bill amount of the order
# placed.
# The discount amount is the sum of all the odd digits in the customers total bill
# amount.
# if no odd digits is present in the bill amount, then discount will be zero.
# input ---------> the input consists of an integer bill amount, representing the
# customers total bill amount.
# output -------> print an integer representing the discount for the given total bill
# amount.
# constraint ---> n>0
# sum of odd digits

def ecommerce_odd_discounts():
    n = input()
    discount=0
    for i in n:
        if i%2 !=0:
            discount += int(i)