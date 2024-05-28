# Sum of even numbers
# Implement a program to find sum of even number between x and y both are
# inclusive.
# input -----> two int values
# constraint-> no
# output ----> sum of even numbers between x and y

def sum_of_even_numb():
    x = int(input('Enter the starting Value'))
    y = int(input('Enter the ending Value'))
    e=0
    for i in range(x, y+1):
        if i%2 ==0:
            e += i
    print(e)

sum_of_even_numb()