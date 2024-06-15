# print Pyramid pattern with fixed digit in every row
#    1
#   22
#  333
# 4444

def pyramid_digit_row():
    n=4
    for i in range(n):
        print(' '*(n-i-1)+str(i+1)*(i+1))

pyramid_digit_row()