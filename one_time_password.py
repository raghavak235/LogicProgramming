# A company wishes to devise an order confirmation procedure.
# They plan to require an extra confirmation instead of simply auto-confirming
# the order at the time it is placed.
# for this purpose, the system will generate one time password to be shared with
# the customer.
# The customer who is placing the order has to enter the OTP to confirm the
# order.
# The OTP generated for the requested order ID, as the product of the digits in
# orderID.
# Write an algorithm to find the OTP for the OrderID.
# input -----> an integer representing order id

def one_time_password():
    order_id = (input())
    otp = 1
    for i in order_id:
        otp = otp * int(i)
    print(otp)


one_time_password()