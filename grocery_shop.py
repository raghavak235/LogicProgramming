# There was a grocery shop. Shopkeeper would like to keep trasactions as simple as he can.
# Hence, he used to take money as whole number. To optimize trasactions,
# he decided if someone buys groceries from his shop, he will round money to the nearest whole number having zeros as last digit.
# Write a program to help shopkeeper to make trasactions much simple.
#
# Input Format
#
# a number
#
# Constraints
#
# no
#
# Output Format
#
# nearest int value which ending with 0
#
# Sample Input 0
#
# 17
# Sample Output 0
#
# 20


def grocery_shop():
    int_value = 17
    while True:
        if int_value%10 == 0:
            print(int_value)
            break
        else:
            int_value +=1
