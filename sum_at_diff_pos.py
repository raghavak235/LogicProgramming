# sum of first and last, second and second last and so on
# Implement a program to find the sum of first and last, second and second last
# and so on in an array.
# input -----> size and array elements
# con -------> no
# output ----> print sum of first and last, second and second last and so on

def sum_at_first_last_second_second_last():
    n=5
    l = [1,2,3,4,5]
    i = 0
    j =n-1
    while i<=j:
        print(l[i]+l[j])
        i +=1
        j +=1

