# Sum of digits between two numbers
# Create a function that sums the total number of digits between two numbers
# inclusive.
# for example,
# if the numbers are 19 and 22, then (1+9)+(2+0)+(2+1)+(2+2)=19.
# input ----------> a number from the user
# constraints ----> no
# output ---------> sum of digits

def inclusive_sm():
    n1 = int(input())
    n2 = int(input())
    digits_sum = 0
    for i in range(n1, n2+1):
        num_str = str(i)
        digits_sum += int(num_str[0]) + int(num_str[1])
    print(digits_sum)

inclusive_sm()
