# Video share is an online video sharing platform. The company has decided to rate its users channels based on the sum total of the number of views received online and the subscribers. This sum total is referred to as user points. The rating will be given according to the below charts.
# User points rating
# 30-50 Average
# 51-60 Good
# 61-80 Excellent
# 81-100 Outstanding
#
# Input Format
#
# points value
#
# Constraints
#
# points>=30 and points<=100
#
# Output Format
#
# rating
#
# Sample Input 0
#
# 55
# Sample Output 0
#
# Good

def ratings():
    n=55
    if n >= 30 and n <= 100:
            if n >= 30 and n <= 50:
                print("Average")
            elif n >= 51 and n <= 60:
                print("Good")
            elif n >= 61 and n <= 80:
                print("Excellent")
            else:
                print("Outstanding")
    else:
        print("invalid")