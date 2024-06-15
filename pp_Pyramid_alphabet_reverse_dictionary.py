# Pyramid pattern with alphabet symbols in reverse of dictionary order
#    D
#   D C
#  D C B
# D C B A

def reverse_dict_order():
    n=4
    for i in range(n):
        print(' '*(n-i-1), end='')
        for j in range(i+1):
            print(chr(64+n-j), end=' ')
        print()

reverse_dict_order()