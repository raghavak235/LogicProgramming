# square pattern with provided fixed digit in every row
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
def square_fixed_digit():
    n=4
    for i in range(n):
        print((str(i+1)+' ')*n)

square_fixed_digit()