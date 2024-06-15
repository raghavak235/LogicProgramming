
# Inverted Right Angle Triangle pattern with digits
# 1 2 3
# 1 2
# 1


def inverted_right_digits():
    n=3
    #  If you don't have the same values in all the rows, you need to take 2 nested loop
    for i in range(n):
        for j in range(n-i): # inside row we need need n-i number of elements to be printed
            print(j+1, end=' ')
        print()

inverted_right_digits()