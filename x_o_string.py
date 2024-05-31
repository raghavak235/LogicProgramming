# X's and O's, Nobody knows
# Create a function that takes a string,
# check if it has the same number of x's and o's and returns either true or false.
# Rules:
# 1. return boolean value true or false.
# 2. returns true if the amount x's and o's are the same.
# 3. returns false if they are not the same amount.
# 4. the string can contain any character.
# 5. when 'x' and 'o' are not in the string, return true.
#
def count_of_x_and_y():
    n = input()
    if n.count('x') == n.count('o'):
        print('True')
    elif n.count('x') != n.count('o'):
        print('False')
    elif 'x' in n and 'o' in n:
        print('True')