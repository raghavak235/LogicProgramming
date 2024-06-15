# he cosmetic company "BeauityMe" wishes to know the alphabetic product code from the product barcode.
# The barcode of the product is a numeric value and the alphabeitc product is a string value tagged 'a-j'.
# The alphabetic range 'a-j' represents the numeric range '0-9'.
# To produce the alphabetic product code. each digit in the numeric barcode is replace by the corresponding matching letters.
# Write an algorithm to display the alphabetic product code from the numeric barcodes.
#
# Input Format
#
# an integer value
#
# Constraints
#
# no
#
# Output Format
#
# a character
#
def beautify_me():
    s='abc'
    for i in s:
        print(ord(i)-97)