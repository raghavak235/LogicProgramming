# Magic Date
# Program to read date, month and year from the user and check whether it is
# magic date or not.
# Here are the rules for magic date.
# 1) mm*dd is a 1-digit number that matches the last digit in YYYY
# 2) mm*dd is a 2-digit number that matches the last two digits in YYYY
# 3) mm*dd is a 3-digit number that matches the last three digits in YYYY

def magic_date():
    date_inp = input()
    month, date, year = date_inp.split('-')[0], date_inp.split('-')[1], date_inp.split('-')[2]
    month_len = len(month)
    if len(str(int(month) * int(date))) == 1 and int(month) * int(date)  == int(year[3]):
        print('magic date')
    elif len(str(int(month) * int(date))) == 2 and int(month) * int(date)  == int(year[2:]):
        print('magic date')
    elif len(str(int(month) * int(date))) == 3 and int(month) * int(date)  == int(year[1:]):
        print('magic date')
    else:
        print('Not magic date')
magic_date()

# Another Implementation:
L=[i for i in input().split("-")]
print(str(L[2].endswith(str(int(L[0])*int(L[1])))).lower())