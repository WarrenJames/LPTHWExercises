# Excercise 11: Asking Questions
# Most of what software does is the following:
#   Take some kind of input from a person.
#   Change it
#   Print out something to show how it changed.


# prints "How old are you?" on the same line(,) as variable "age" (which equals
#   user's input)
print "How old are you?",
age = raw_input()
# prints "How tall are you?" on the same line(,) as variable "height" (which
#   equals user's input)
print "How tall are you?",
height = raw_input()
# prints "How much do you weigh?" on the same line(,) as variable "weight"
#   (which equals user's input)
print "How much do you weigh?",
weight = raw_input()

# prints string "So, you're (raw formatter modulo) old", (raw formatter modulo)
#   tall and (raw formatter modulo)
#   and (raw formatter modulo) pounds. Modulo(%) is equal to age, height, weight
print "So, you're %r old, %r tall and %r pounds." % (
    age, height, weight)


# raw_input() takes the exact input that the user types and passes it back as
#   a string

# input() takes the input and does an evaluation eval() before passing back as
#   a string.

# with python 3 input() is the same as raw_input() in python 2.7 and
#   eval(input()) is subsitutes as input() in python 3
