# Sum of prime Digits
# Implement a program to calculate sum of prime digits present in the given
# number
# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of prime digits
# prime ===> prime numbers
# prime digits ===========> single 0-9



# ----> prime digits from 0 to 9 ====> 2,3,5,7, divisible by 1 and itself

#  Only asking the prime digits which means 0-9, we should write logic for 2,3,5,7 nums
def sum_of_prime_digits():
  print(sum([int(i)  for i in list(input()) if i in '2357']))

sum_of_prime_digits()