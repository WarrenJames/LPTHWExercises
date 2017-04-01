# Exercise 6. Strings and Text

# Quick practice as a refresher from previous Exercise.
var = 2

print "Hi, My name is %s." % (var)

# End refresher

# A string is usually a bit of text you want to display to someone or "export" out of the program you are writing.
# Python knows you want something to be a string when you put either "" or '' around the text.

# If you want multiple formats in your string to print multiple variables you need to put them inside () separated by , (commas).

# Programmers love saving time at at your expense by using annoyingly short and cryptic variable names.

# x = "There are 10 types of people." %d stands for a integar (whole number).
x = "There are %d types of people." % 10
# binary is referred to as "binary"
binary = "binary"
# do_not is refferred to as "don't"
do_not = "don't"
# y is referred to as "Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints as "There are are 10 types of people."
# Prints as "Those who know binary and those who don't."
print x
print y

# Prints as "I said:There are 10 types of people."
print "I said: %r" % x
# Prints as "I also said: 'Those who know binary and those who don't.'."
print "I also said: '%s'." % y

# hilarious is referred to as "False"
hilarious = False
# joke evaluation is refferred to as "Isn't that joke so funny?! False"
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints as "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

# w is refferred to as "This is the left side of..."
w = "This is the left side of..."
# e is refferred to as "a string with a right side."
e = "a string with a right side."

# Prints as "This is the left side of...a string with a right side."
print w + e

# %r is for debugging and also stands for raw
