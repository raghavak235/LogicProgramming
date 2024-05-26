# The e-commerce company Bookshelf wishes to analyse its monthly sales data
# between minimum range 30 to max range 100.
# The company has categorized these book sales into four groups depending on
# the number of sales with the help of these groups the company will know
# which stock they should increase or decrease in their inventory for the next
# month.
# the groups are as follows
# sales_range     groups
# 30-50 ------------------> D
# 51-60 ------------------> C
# 61-80 ------------------> B
# 81-100 -----------------> A
# write an alg to find the group for the given book sale count.
# input--------> an integer salesCount represent total sales of a book
# output-------> a character representing the group of given sale count
# constraint---> 30<=saleCount<=100

def book_count():
    n = int(input('Enter the value'))
    if 30<=n<=100:
        if 30 <= n <=50:
            print('D')
        elif 51 <= n <= 60:
            print('C')
        elif 61<=n<=80:
            print('B')
        else:
            print('A')

    else:
        print('invalid')
