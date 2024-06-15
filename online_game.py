# You are playing an online game. In the game, a numbers is displayed on the screen. In order to win the game,
# you have to count the trailing zeros in the factorial value of the given number.
# Write an algoritm to count the trailing zeros in the factorial value of the given number.
#
# Input Format
#
# an integer num, representing the number displayed on the screen.
#
# Constraints
#
# no
#
# Output Format
#
# the count of trailing zeros in the factorial of the given number.



def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
def online_games():
     # Should count only ending zeros
    #  7!=5040 Should count only ending zeros
    n =7
    value = factorial(n)
    c=0
    while value !=0:
        if value%10 == 0:
            c=c+1
        else:
            break
        n=n//10
    print(c)

