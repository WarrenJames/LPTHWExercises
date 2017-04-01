# Excercise 13: Parameters, Unpacking, Variables

# Line 12 has "import". This is how you add feaures to your script from
#   the Python feature set. Rather than give you all the features at once,
#   Python asks you to say what you plan to use. This keeps your programs small,
#   but it acts as documentation for other programmers who read your code later.


# agrv is the "argument variable". This variable holds the arguments you passes
#   to your Python script when you run it.
# from system module import 'arguement variable'
from sys import argv

#   modules give you features!

# script, first, second, third fourth, and ham all equal arguement variable
script, first, second, third, ham = argv

# fourth variable is equal to users raw input
ham = raw_input()

# prints "The script is called:" and (,) script variable on one line
print "The script is called:", script
# prints "Your first variable is:" and (,) first variable on one line
print "Your first variable is:", first
# prints "Your second variable is:" and (,) second variable on one line
print "Your second variable is:", second
# prints "Your third variable is:" and (,) third variable on one line
print "Your third variable is:", third
# prints "Your fourth variable is: (raw modulo)" modulo is equal to variable
#   fourth which is equal to raw input
print "Your fourth variable is: %r" % ham

# the difference between argv and raw_input() has to do where the user is required
#   to give input. If they give you script inputs on the command line, then you
#   use agrv. If you want them to input using the keyboard while the script is
#   running, then use raw_input().
