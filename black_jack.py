# Implement the following function
# int BlackJack(int n1,int n2);
# the function accepts two +ve integers n1 and n2 as its arguments.
# Implement the function on given two values to return an int value as follows
# return whichever value is nearest to 21 without going over. Return if they go
# both go over.
# input --------> two int values n1 and n2
# constraint ---> no
# output -------> 0 or n1 or n2

def black_jack():
    n1 = int(input())
    n2 = int(input())

    # You can do the difference operation.
    # You can the difference with inputs which ever diff is small, the  input number near to the 21
    diff_1st = 21 - n1
    diff_2nd = 21 - n2
    if diff_1st < diff_2nd:
        print(n1)
    elif diff_1st > diff_2nd:
        print(n2)
    elif n1> 21 and n2 > 21:
        print('0')

    # Another Implementation
    # You can verify using both input comparisons
    if n1 > n2 and (n1 < 21 and n2 < 21):
        print(n2)
    elif n1 < n2 and (n1 < 21 and n2 < 21):
        print(n1)
    elif n1 >21 and n2 > 21:
        print(0)

black_jack()