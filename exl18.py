# Excercise 18: Names, Variables, Code, Functions
# Functions do three things:
#   They name pieces of code the way variables name strings and numbers.
#   They take arguments the way your scripts take argv
#   Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands"

# First we tell python we want to make a function using def for "define".
#   On the same line as def we give the function a name. In this case we just
#   called it print_two but it could also be "peanuts". It doens't matter,
#   except that the function should have a short name that says what it does.

# without the asterisk, python will believe print_two accepts 1 variable.
# Tells python to take all the arguments to the function and then put them in
#   args as a list. It's like agrv but for functions. not used too
#   often unless specifically needed
## def print_two(*args):
##    arg1, arg2 = args
##    print "arg1: %r, arg2: %r" % (arg1, arg2)

# okay that *args is actually pointless
# define(function) name is print_two_again(arg1, arg2): <-- don't forget the ":"
#   it tells what print_two_again consists of, which so happens to be printing
#   "Senor: (raw modulo), El: (raw modulo)" % modulo is (arg1, arg2) or
#   (James, Warren)
def print_two_again(arg1, arg2):
    print "Senor: %r, El: %r" % (arg1, arg2)

# this just takes one argument
# define(function) print_one(variable arg1 which equals First): <-- consists of
# print "the: %raw modulo" raw modulo is arg1 which is "first"
def print_one(arg1):
    print "the: %r" % arg1

# this one takes no arguments
# define print_none(): empty call expression consists of printing
#    "I got nothin'."
def print_none():
    print "I got nothin'."


## print_two("James","Warren")
# lines 43 to 45 all call functions
# calls print_two_again("James", "Warren") for arg1 and arg2
# calls print_one("First!") for arg1
# calls print_none() with no arguments
print_two_again("James","Warren")
print_one("First!")
print_none()
