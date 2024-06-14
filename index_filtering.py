# INDEX FILTERNING
# Create a function that takes two inputs: idx (an array of integers) and str (a
# string). The function should return another string with the letters of str at each
# index in idx in order.
# input ----------> a string followed by size and an array
# constraint -----> output must be in lower case but input many not be.
# output ---------> a string contained in the specified locations given in the array.

def index_filter():
    stri='She is the love of my love'
    n=3
    l=[7,11,14]
    for i in range(n):
        print(stri[l[i]])

index_filter()