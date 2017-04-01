# Exercise 5: More variables and Printing
# This excersie will being using a format string. Every time you put "" (double-quotes) around a  piece of text it makes a string.
# Makes strings with variables embedded in them

# my_name is the variable name that you call to refer to Zed A. Shaw.
name = 'Zed A. Shaw'
# my_age is the variable name that you call to refer to Zed A. Shaw.
my_age = 35 # not a line
# my_height would display as "74" with added comment of inches (which will not display # inches)
height = 74 # centimeters
# my_height would display as "180" with added comment of inches (which will not display # lbs)
# You are able to round a function like this round(1.9) displays as "2".\
my_weight = round(180.23) # lbs
# my_eyes displays as Blue
eyes = 'Blue'
# my_teeth displays as White
my_teeth = 'White'
# my_hair displays as Brown
hair = 'Brown'


# prints "Let's talk about Zed A. Shaw." code shows %s equals my_name or "Zed A. Shaw."
print "Let's talk about %s." % name
# prints "He's 74 inches tall." code shows %d equals my_height or "74"
print "He's %d inches tall." % height
# prints "He's 180 pounds heavy. "
print "He's %d pounds heavy." % my_weight
# prints "Actually that's not too heavy." onto terminal.
print "Actually that's not too heavy."
# prints "He's got Blue eyes and Brown hair." showing first % equals my_eyes or "Blue" and second % equals "Brown"
#seperate each value by comma
print "He's got %s eyes and %s hair." % (eyes, hair)
# prints "His teeth are usually White depending on the coffee." % shown to equal my_teeth or "White"
print "His teeth are usually %s depending on the coffee." % my_teeth

# prints as "If I add 35, and 74, and 180 I get 289." code shows that first % equals my_age, second % equals my_height
# third % equals 180. and third % is the sum of all variables added together
print "If I add %d, %d, and %d, I get %d." % (my_age, height, my_weight, my_age + height + my_weight)
# using a numerial value is not a valid variable name. They need to start with a character.
# %s, %r and %d are referred to as "formatters". Which tell Python to take the variable on the right and put it into replace the %s with it's value.
# %s is for string
# %d is for integar
# %f is for float first number will show many decimal places. (%1.55f)
# "{}" can be used in replacement for % after statement add .format("World")
