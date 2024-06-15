# A spy wants to send some secret information to the government.
# As the data is very important, he encrypts the message by encoding by adding some extra characters.
# the original message has only upper case letters and numbers, while the extra characters are madeup of lowercase letters
# and special characters. Can you help the receiver in designing a program that accepts the message and returns the secret information.
#
# Input Format
#
# a string from the user
#
# Constraints
#
# no
#
# Output Format
#
# original message

def secret_message():
    s ='Wel1c%OmE'
    for i in s:
        if i.isdigit() or i.isupper():
            print(i, end=' ')

secret_message()