# Free Coffee Cups
# For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups.
# Implement a program that takes n cups bought and print as an integer the
# total number of cups I would get.
# input -------------> n number of cups from user
# constraints -------> n>0
# output ------------> number of cups present have
# buy 2 get 1 free
# 5+5/2
# 5+2=7
# 2+1
# 2+1
# 1+0

def cofffee_cups():
    n =int(input())
    print(n + n/6)