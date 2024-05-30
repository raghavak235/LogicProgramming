# LBP48
# Accept video length in minutes the format is mm:ss in String format,
# create a function that takes video length and return it in seconds.
# input --------> video length in mm:ss
# constraint----> no
# output -------> length in seconds

def min_to_secs():
    n = input().split(':')
    print(int(n[0])*60 + int(n[1]))