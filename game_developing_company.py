# a game developing company has developed a math game for kids called "Brain Fun".
# The game is for smartphone users and the player is given list of N positive numbers and a random number K.
# the player need to divide all the numbers in the list with random number k and then need to add all the quotients received in each division.
# the sum of all the quotients is the score of the player.
# Write an algorithm to generate the score of the player.
#
# Input Format
#
# array size, elements and random number k
#
# Constraints
#
# no
#
# Output Format
#
# an int value
#
# Sample Input 0
#
# 5
# 1 2 3 4 5
# 3
# Sample Output 0
#
# 3
def sum_coefficient():
    n=[1,2,3,4,5]
    c=3
    s=0
    for i in l:
        s= s+(i//c)