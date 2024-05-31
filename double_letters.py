# Double Letters
# Create a function that takes a word and returns true if the word has two
# consecutive identical letters.
# input ---------> A string
# constraint-----> No
# output --------> true or false

def double_letters_string():
    n = input()
    found = False
    for i in range(len(n)-1):
        print(i)
        # As you are verifying increasing the i value below, you need to decrease in range func
        print(n[i], n[i+1])
        if n[i] == n[i+1]:
            found = True

double_letters_string()
