# Excercise 12: Prompting People

# variable age is equal to raw_input with prompt of "How old are you? "
age = raw_input("How old are you? ")

# variable height is equal to raw_input with prompt of "How tall are you? "
height = raw_input("How tall are you? ")

# variable weight is equal to raw_input with prompt of "How much do you weigh? "
weight = raw_input("How much do you weigh? ")


# %r is equal to variables age, height, and weight.
print "So you're %r old, %r tall and %r pounds." % (age, height, weight)
# prints as "So you're" (user inputed information) old, (user inputed
#   information) tall and (user inputed information) pounds.

# Study Drill
#   On windows powershell type python -m pydoc (file name)

# pydoc command provides information from documentation for python
#   commands can be found at c:\Python27\Lib\(enter command here)
#   example of commands (open, file, os, and sys)
#   get out of pydoc by typing 'q' to quit  
