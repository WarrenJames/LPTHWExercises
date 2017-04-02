# Exercise 21: Functions Can Return Something

# define function add with a, and b as expressions consist of printing
# "Adding a + b" %d integer modulos are equal to a, and b expressions
# returns sum of a + b expressions like (= in a function)
def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

# define function subtract(with a, and b as expressions) consist of
# printing "Subtracting a - b" integer modulos are equal to a, and b
# returns sum of a minus b
def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

# define function multiply(with a, and b as expressions) consist of
# printing "Multiplying a * b" integer modulos are equal to a, and b
# returns product of a * b
def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

# defines function divide(with a, and b as expressions) consist of
# printing "Dividing a / b" integer modulos are equal to a, and b
# returns sum of a divided by b
def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

# prints string of text "Let's do some math with just functions"
print "Let's do some math with just functions!"

# all numbers added in function expressions replace "a" and "b"
# age variable is equal to add function with (a, b) replaced by (30, 5)
age = add(30, 5)
# height variable is equal to subtract function with (a, b) replaced by (78, 4)
height = subtract(78, 4)
# weight is equal to multiply function with (a, b) replaced by (90, 2)
weight = multiply(90, 2)
# iq is equal to divide function with (a, b) replaced by (100, 2)
iq = divide(100, 2)

# prints "Age: 35, Height: 74, Weight: 180, IQ: 50"
# integer modulos are equal to age, height, weight, iq variables
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
# prints "Here is a puzzle."
print "Here is a puzzle."

# what variable is equal to:
#  Dividing 50 / 2 = 25
#  Multiplying 180 * 25
#  Subtracting 74 - 4500
#  Adding 35 + -4426
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))


# prints onto terminal "That becomes: -4391 Can you do it by hand?"
print "That becomes: ", what, "Can you do it by hand?"
