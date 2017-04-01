# Excercise 16: Reading and Writing Files

# List of commands to remember
#   close -- Closes the file. Like File -> Save.. in your editor.
#   read -- Reads the contents of the file. Can assign the result to a variable
#   readline -- Reads just one line of a text file.
#   truncate -- Empties the file.
#   write('stuff') -- Writes "stuff" to the file.

# from system import arguement variable
from sys import argv

# script name and file name entered are both equal to arguement variable
script, filename = argv
# prints "We're going to erase (filename)" raw string is equal to filestring
print "We're going to erase %r" % filename
# prints "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit CTRL-C (^C)."
# prints "If you do want that, hit RETURN."
print "If you do want that, hit RETURN."
# raw_input("?") asks for users raw input, prompted by a "> "
raw_input("> ")
# prints "Opening the file..."
print "Opening the file..."
# variable target is equal to open(filename, 'w')
# open(filename, 'w') opens the file object in write mode(method).
target = open(filename, 'w')
# prints "Truncating the file. Goodbye!"

# prints "Now I am going to ask you for three lines."
print "Now I am going to ask you for three lines."
# line1 variable is equal to raw_input with "line 1: " in the parameters
line1 = raw_input("line 1: ")
# line2 variable is equal to raw_input with "line 2: " in the parameters
line2 = raw_input("line 2: ")
# line3 variable is equal to raw_input with "line3: " in the parameters
line3 = raw_input("line 3: ")

# target variable with a decimal operator with the write command
# parameters equal string,new line, string, new line, string, new line
# interpolation operator says first string is equal to line1, second string is
# equal to line2, and third string is equal to line3
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# prints "And finally we close it."
print "And finally we close it."
# target variable with decimal operator with the close command closes object
target.close

# TIL: use %s for strings when writing, %r will create '' around output
# TIL: target.truncate() is not needed when opening the filename with write mode
# due to it overwriting the file already.
