# Excercise 14: Prompting and Passing

# this is an import from the sys module "arguement variable"
from sys import argv

# script, and user_name equal argv
script, user_name, mashedpotato = argv
# variable "prompt" equals '> '
chicken = '><> '
mashedpotato = 'you lying ass bitch.'

# prints the string "Hi (string modulo), I'm the (string modulo)"
# modulo's are (user_name variable, and script variable)
print "Hi %s, I'm the %s script." % (user_name, script)
# prints string "I'd like to ask you a few questions"
print "I'd like to ask you a few questions."
# prints "Do you like me (string modulo)" modulo formatter is user_name
print "Do you like me %s?" % user_name
# variable likes is equal to raw_input(prompt variable which is '> ')
likes = raw_input(chicken)

# prints as "Where do you live (string modulo)" modulo formatter is user_name
print "Where do you live %s?" % user_name
# variable lives is equal to raw_input(prompt variable which is '> ')
lives = raw_input(chicken)

# prints as "What kind of computer do you have?"
print "What kind of computer do you have?"
# computer variable equals raw_input(prompt variable which is '> ')
computer = raw_input(chicken)

# prints long string(""") as
#   Alright, so you have said '(raw formatter modulo)' about liking me.
#   You live in '(raw formatter modulo)'. Not sure where that is.
#   and you have a '(raw formatter modulo)' computer. What a load of shit
#   raw formatter modulo is raw_input entered by user (likes, lives, computer)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
and you have a %r computer. What a load of shit. %r
""" % (likes, lives, computer, mashedpotato)

# Study Drills
    # Play Zork and Adventure. Python word based adventure games.
    # change prompt variable to something else entirely
# changed  prompt to chicken
