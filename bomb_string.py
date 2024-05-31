# Find the Bomb
# Write a function that finds the word "bomb" in the given string (not case
# sensitive)
# return "DUCK!" if found, else return "Relax there's no bomb."
# input ---------> a string
# constraint ----> no
# output --------> "DUCK!" or "Relax, There's no bomb."

def bomb():
    n = input()
    if 'bomb' in n:
        print('DUCK')
    print('No Bomb')