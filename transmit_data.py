# A company wishes to transmit data to another server.
# The data consists of numbers only.
# To secure the data during transmission, they plan to reverse the data during
# transmission,
# they plan to reverse the data first.
# Write an algorithm to reverse the data first
# input -----> an integer data, representing the data to be transmitted
# output ----> print an integer representing the given data in reverse form

def reverse_the_data():
    data = input()
    data_reverse=''
    for i in range(len(data)-1, -1, -1):
        data_reverse += data[i]

    print(int(data_reverse))





 # USING while
def reverse_number():
    data_num = int(input())
    reverse_number = 0
    while data_num > 0:
      last_num = data_num % 10   #Use number % 10 to get the last digit of the current number.
      print(last_num)
      reverse_number = last_num + reverse_number * 10 # Multiply reversed_num by 10 (to shift its digits to the left) and add the extracted digit.
      print(reverse_number)
      data_num = data_num//10  #Use integer division number // 10 to remove the last digit from the current number.
      print(data_num)
    print(reverse_number)

reverse_number()