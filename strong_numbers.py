# sum of strong numbers in an array
# Implement a program to read an array elements and print sum of all strong
# numbers in array.
# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all strong numbers



def strong_number():
     n =int(input())
     num=n
     s=0
     while (n >0):
         digit = n%10
         fact=1
         for i in range(1, digit+1):
             fact =  fact*i
         s += fact
         n = n//10

     print(s)
     if s==num:
         print("Strong  Num")

strong_number()