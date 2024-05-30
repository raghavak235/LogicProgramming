# An e-Commerce company plans to give thier customers a discount for the
# newyears holiday. The discount will be calcualted on the basis of the bill
# amount of the order place. The discount amount is the productof the sum of
# all odd digits and the sum of all even digits of the customers total bill amount.
# input ----> an integer bill amount, representing the total bill amount of the
# customer.
# output ---> print an integer representing the discount amount for the given total
# bill.

def odd_even_prod_discount():
    bill = input()
    even_num, odd_num =0,0
    for i in bill:
        if int(i)%2 == 0:
            even_num += int(i)
        else:
            odd_num += int(i)

    print(int(even_num) * int(odd_num))


odd_even_prod_discount()