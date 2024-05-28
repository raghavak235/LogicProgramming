# ofSum of Digits
# Implement a program to calculate sum of digits present in the given number
# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of digits

def sum_of_digits():
    n = int(input('Enter the number'))
    output_list = []
    while n !=0:
        d = n%10
        n = n//10
        output_list.append(d)

    print(sum(output_list))

    #Another Implementation
    s=0
    while n != 0:
        d=n%10
        s= s +d
        n = n //10
    print(s)


sum_of_digits()

