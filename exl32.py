# Exercise 32 Loops and Lists

# the_count variable is equal to list with items: 1, 2, 3, 4, and 5
the_count = [1, 2, 3, 4, 5]

# fruits variable is equal to list with items: apples, oranges, pears,
# and apricots
fruits = ['apples', 'oranges', 'pears', 'apricots']
# change variable is equal to list with items: 1, pennies, 2, dimes,
# 3 and quarters
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

""" this first kind of for-loop:
for (item) in the_count: print "This is a count %/decimal modulo" %/ modulo is
equal to list item.  """
for number in the_count:
    print "This is count %d" % number

""" you are able to use any name when referring to list items
 for (list item) in fruits variable: print "A fruit of type: %/string modulo"
 string modulo is equal to (list item)
"""
for fruit in fruits:
    print "A fruit of type: %s" % fruit

""" also we can go through mixed lists too
notice we have to use %/raw modulo since we don't know what's in it
for (item) in change: print "I got %/raw modulo" raw modulo is equal to (item) """
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
# elements variable is equal to empty list
elements = []

""" then use the range function to do 0 to 5 counts
for item in range (0 through 5): prints onto terminal "Adding %/digit modulo to
the list." modulo is equal to list item. then appends(item) into elements
variable """
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists are able to understand
    elements.append(i)

# now we can print them out too
# for item in elements variable: print element was: (list item)
for i in elements:
    print "Element was: %d" % i

# each for-loop would loop through until list or range is finished
