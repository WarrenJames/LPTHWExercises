import math


# ----- Variables -----
"""
variables are containers for data.
Only start a variable with with lowercase letter have uppercase/lowercase letters,
numbers and underscores_ (no spaces).

you are also able to redefine variables.

Example variables:
"""

var = 5
twoWords = "Two words."
under_score = 10

print "variable: "
print var

var += 10
print "redefined variable: "
print var


# ----- Math -----
"""
Python is capable of doing math.

Uses order of operations: Pemdas
(Parenthesis, Exponents, Multiplication/Division, Addition/Subtraction)

"""
# addition
2 + 4
10 + 239

aOne = 10
aTwo = 2

aTwo = aOne + aTwo

print "atwo variable should now be equal to: 12"

# subtraction
11 - 10
78 - 100

sOne = 24
sOne -= 2

print "sOne variable should now be equal to: 22"

# multiply
50 * 50
10 * 5

mOne = 15
mOne *= 3
print "mOne variable should now be equal to: 45"

# divide
10 / 2
100 / 30

# parenthesis
(50 + 10) * 10
30 + (25 / 5) - 10

# power
5 ** 2 # five squared
10 ** 10
pOne = 5
pOne **= pOne

print "pOne variable should now be equal to: 3125"

# remainder
11 % 5 # 1
100 % 99 # 1
rOne = 7 % 3

print "rOne should now be equal to: 1"

"""
Python uses both full numbers (integers) and ones with a decimal place
(floating point). You can specifically define a floating point or
integer, by using a decimal or python functions such as:
"""
# floating point:
float(3) # returns 3.0
float(3)/2 # returns 1.5

# integers:
int(3.9) # returns 3
int(3.1) # returns 3

# more math symbols by importing math module in Python
"""
abs() - absolute value
sin() - sin of
cos() - cosine of
ceil() - round up
power() - power (aka **)
"""

# ----- Strings -----
"""
Represents a string of any characters, and are declared by quotation marks.
you can use both double-quotations "" or single-quotations '' depending on
your preference.
"""

strOne = "This is a string with double-quotations."
print strOne

strTwo = 'This is a string with single-quotations.'
print strTwo

strThree = strTwo + " You can also add strings together."
print strThree

# str() is used to convert to a string

num = 10
strFour = strThree + str(num)

print strFour

# you are also able to place values within Strings
strFive = "%d as an integer" % (num)
print strFive

strSix = "%f for floating point" % (num)
print strSix

strSeven = "or control how many numbers after decimal with %.3f" % (num)
print strSeven





# ----- Tuples -----

# ----- Lists -----

# ----- Dictionaries -----

# ----- Functions -----
"""
"""
def basicFunction():
    pass
