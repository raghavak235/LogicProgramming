

def odd_or_even(n):
    if n > 0:
        if n%2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
    else:
        print("Invalid Number")




# updated version

def single_line():
    n = int(input('Enter the value'))
    # single line if else condition
    # value if condition true else value
    print("invalid" if n < 0 else ("even" if n%2==0 else "odd"))