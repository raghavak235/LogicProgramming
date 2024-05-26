# Given an integer n, perform the following conditional actions,
# if n is odd, print weird,
# if n is even and in the inclusive range of 2 to 5, print Not Weird.
# if n is even and in the inclusive range of 6 to 20, print Weird.
# if n is even and greater than 20, print Not Weird.

# input-----> a number from the user
# contraint-> 1<=n<=100
# output----> Weird or Not Weird

def conditional_actions():
    n = int(input('enter the value'))
    if 1<=n<=100:
        if n%2 != 0:
            print('Weird')
        else:
            if 2 <= n <= 5:
                print('Not Weird')
            elif 6 <= n <= 10:
                print('Weird')
            else:
                print("Not Weird")

conditional_actions()