# Andy, Ben and Charlotte are playing a board game.
# The three of them decided to come up with a new scoring system.
# A player's first initial ("A","B" & "C") denotes that players scoring a single point.
# Given a string of capital letters. returns an array of the player's scores.
# input --------------> A String
# constraint ---------> No
# output -------------> score

def board_game():
    n =input()
    print(n.count("A"), n.count('B'), n.count('c'))