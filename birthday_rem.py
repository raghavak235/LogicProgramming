# Check Birth Day
# Lisa always forgets her birthday which is on the 5th July.
# So develop a function/method which will be helpful to remember her birthday.
# The function/method checkBirthday return an integer 1, if it is her birthday
# else return 0.
# the function/method checkBirthday accepts two arguments.
# Month, a string representing the month of her birth and day, an integer
# representing the data of her birthday.
# input -----------> month & day
# constraints -----> no
# output ----------> 1 or 0

def birthday():
    month= input()
    day = int(input())
    if month.lower()=='july' and day == 5:
        print('1')
    else:
        print('0')
