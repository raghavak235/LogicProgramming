# Create PIN using Three given numbers
# "Secure Assets Private Ltd", a small company that deals with lockers has
# recently started manufacturing digital locks which can be locked and unlocked
# using PINs (passwords).
# You have been asked to work on the module that is expected to generate PINs
# using three input numbers.
# The three given input numbers will always consist of three digits each
# i.e. each of them will be in the range >=100 and <=999.
# Bellow are the rules for generating the PIN.
# 1. The PIN should made up of 4 digits.
# 2. The unit (ones) position of the PIN should be the least of the units position
# of the three numbers.
# 3. The tens position of the PIN should be the least of the tens position of the
# three input numbers.
# 4. The hundreds position of the PIN should be least of the hundreds position of
# the three numbers.
# 5. The thousands position of the PIN should be the max of all digits in the three
# input numbers.
# input ----------> three numbers
# constraints ----> all the numbers must be in the range of >=100 and <=999
# output ---------> PIN value

def generate_pin():
    n1 = [int(i) for i in input()]
    n2 = [int(i) for i in input()]
    n3 = [int(i) for i in input()]
    min_1 = min(n3[2], n2[2], n1[2])
    min_10 = min(n3[1], n2[1], n1[1])
    min_100 = min(n3[0], n2[0], n1[0])
    max_v = max(max(n3), max(n2), max(n1))
    formula= max_v* 1000 + min_100 * 100 + min_10*10 + min_1
    print(formula)

generate_pin()
