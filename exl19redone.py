# Exercise 19: Study drill
#  Create a function of my own design and run it 10 different ways
from sys import argv
script, filename = argv

def bottles_of_beer(on_the_wall, bottles_to_go):
    print """%s bottles of beer on the wall\n%s bottles of beer!
    Take one down, pass it around %s bottles of beer""" % (on_the_wall, on_the_wall, bottles_to_go)

bottles = 99
bottlesLeft = bottles - 1

bottlefile = open(filename, 'r')
bottles95 = bottlefile.read()
bottles94 = 94


bottles_of_beer(bottles, bottlesLeft)
bottles_of_beer(99 - 1, 98 - 1)
bottles_of_beer(97, 96)
bottles_of_beer(96, bottles95)
bottles_of_beer(bottles95, bottles94)
bottles_of_beer('94', '93')

bottlefile.close


#                               Today I Learned:
# refer to lines 13 and 14. File must be opened before being read
#   consider python reading the code in numerical order. make a variable
#   open the filename in read mode before making a variable to have bottlefile
#   with the reader decimal operator with no parameters
#   ie.  open(filename, 'r') comes before bottlefile.read()
# when refering to a read file in an expression anything written is referred to
#   as a string.
#   ie.   the number 95 written in file will not work with %d
#
# you cannot use /n linebreaks in expressions
#   ie.  bottles_of_beer(96, bottles95\n)
# you are able to call a function within a function
