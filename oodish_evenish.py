# Oddish or Evenish
# Create a function that determines whether a number is Oddish or Evenish.
# A number is Oddish if the sum of all of its digits is Odd,
# and number is Evenish if the sum of all of its digits is even,
# if a number is Oddish return Oddish else return Evenish.

def sum_odd_even():
    l=[int(i) for i in input()]
    print('Evenish')if sum(l)%2 == 0 else print('Oddish')


sum_odd_even()