# Student Rewarded
# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
# 'A': Absent.
# 'L' : Late.
# 'P': Present.
# A student could be rewarded if her or his attendance record doesn't contain
# more than one 'A' (absent) or
# more than two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his
# attendance record.
# input ------> a string from the user
# con --------> non empty string

def student_rewards():
    n  = input()
    a_count = n.count('A')
    l_count=0
    if a_count ==2:
        print("No")
    if "LLL" in n or n.count('LLL') > 1:
        print("No")
    print("Yes")


