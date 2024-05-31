# Determine the color of a chess board square
# You are given coordinates, a string that represents the coordinates of a square
# of the chess board. bellow is the chess board for your reference.
# Return True if the saquare is in white, and false if the square is in Black.
# The coordinates will always represent a valid chess board square. The
# coordinates will always have the letter first, and the number second.
# input ----------> a string
# constraint -----> length of the string is 2, a<=c[0]<=h and 1<=c[1]<=8
# output ---------> true or false

def chess_board():
    s=input()
    x = ord(s[0]-96) # the input is given as a, we need to convert using ascii. ord('a') returns 97, which is the ASCII value for the character 'a'.
    y=ord(s[1])
    print(x%2 != y%2)