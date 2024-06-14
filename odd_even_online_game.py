# Odd Even Online Game
# You are playing an online game. In the game, a list of N numbers is given. The
# player has to arrange the numbers so that all the odd numbers of the list come
# after even numbers. Write an algorithm to arrange the given list such that all
# the odd numbers of the list come after the even numbers.
# input -------> size and array elements
# con ---------> no
# output ------> all even numbers and odd numbers.

def online_game():
    n = [1,2,3,4,5]
    even_list,odd_list=[],[]
    for i in n:
        if i%2==0:
            print(i)
            even_list.append(i)
        else:
            odd_list.append(i)