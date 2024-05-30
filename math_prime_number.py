# Jackson, a math student, is developing an application on prime numbers. for
# the given two integers on the display of the application, the user has to identify
# all the prime numbers within the given range (including the given values).
# afterwards the application will sum all those prime numbers. Jackson has to
# write an algorithm to find the sum of all the prime numbers of the given range.
# Write an algorithm to find the sum of all the prime numbers of the given range.
# input -----> two space separated integers RL and RR.
# output ----> sum of the prime numbers between RL and RR




def math_student_prime_number():
    lr = int(input())
    rr = int(input())
    prime_number_sum = 0
    for i in range(lr, rr+1):
        # Should iterate from 2 to i ex:10
        for j in range(2, i):
            if i%j == 0: # 10/2 ==0
                break
        else: # if no divisions are there, then comes to else part
            print('Prime', i)
            prime_number_sum += i
    print(prime_number_sum)



math_student_prime_number()