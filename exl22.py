from sys import argv
script, argVar = argv

# Exercise 22: What Do You Know So Far?

# **Exercise 0: The Set Up**

#  N/A

# **Exercise 1: A Good First Program**
print 'print is to print a string onto the terminal.'

#**Exercise 2: Comment And Pound Characters**

# <- the octothorpe/pound/hash/mesh symbol comments out a line

# **Exercise 3: Numbers and Math**
3 + 3 # plus symbol is for addition
8 - 2 # minus symbol is for subtraction
48 / 8 # slash symbol is for division
3 * 3 # asterisk symbol is for multiplication
99 % 10 # percent symbol is for remainder (also used as modulo/modulus)
9 < 11 # less-than symbol
10 > 2 # greater-than symbol
6 <= 24 # less-than-equal symbol
10 >= 12 # greater-than-equal symbol

# **Excercise 4: Variables and Names**
underscores_in_variables = 1337

floatingPoint = 7.0 # numbers with decimals
integer = 7 # numbers without decimals / whole numbers

# **Exercise 5: More Variables and Printing**
rOne = 'representation modulus'
rTwo = 'raw data'

print "percent sign that gives value to the string is called a %s" % ('modulus')
print "a %s modulus is to put value to a %s." % ('string', 'string')
print "a modulus for numbers(digits) is %d!" % underscores_in_variables
print "a %r is for %r, useful for debugging. Prints with quotes." % (rOne, rTwo)

# **Exercise 6: Strings and Text

print "double-quotes."
print 'single-quotes.'

# **Exercise 7: More Printing**

plusOne = 'the plus symbol can be used for joining strings with'
plusTwo = 'out spaces.'
commaOne = 'The comma can be used for joining strings on same line with spaces.'

print plusOne + plusTwo,
print commaOne

# **Exercise 8: Printing, Printing**
print "%r is a Boolean value that doesn't need quotes." % True
print "%r is also a Boolean value that doesn't need quotes." % False

# **Exercise 9: Printing, Printing, Printing**
print "the backslash is used to escape characters."
print "use the command \n to print on a new line."
print """
        triple-quotes gives you the ability to set off
        multiple lines of text."""

# **Exercise 10: What was that?**
print "use \\ to escape backslash."
print 'use \' to escape a single quote in a string.'
print "use \" to escape double-quotes in a string."
print "This is\rThe carriage return in a string returns to the start of line."
print "\tBackslash tab is used to use a tab in a string."
print '''You
 can
  use
single
-quotes
 as well'''

# **Exercise 11: Asking Questions**
getInputFromUser = raw_input()
print """You can then pass the input into a string...
%r""" % getInputFromUser

# **Exercise 12: Prompting people.
alternativeWayToPrompt = raw_input('Prompt for user to type: ')

# **Exercise 13: Parameters, Unpacking, Variables**
print "Read the top of the code to see how to import argument variables."
print "you can pass the info from arguments to variables: %r" % argVar
print """Module is the name for collections of extra code that can be
imported into python (aka libraries). Packing and unpacking values is to get
information in and out of an argument variable(argv)."""

# **Exercise 14: Prompting and Passing**
print """a prompt is a character or a string that the scripter can specify
to ask for info from the end user"""

# **Exercise 15: Reading Files**
