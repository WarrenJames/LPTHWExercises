# Excercise 15: Reading Files

# from system import "arguement variable"
from sys import argv

# script and(,) filename is equal to "arguement variable"
# script is "exl15.py" and filename is "exl15_sample.txt" when typing into
#   powershell/terminal.
script, filename = argv

# variable is equal to open(filename) refer to line 7.
txt = open(filename)

# prints "Here's your file %r (raw string):" %raw representation is filename
# arguement variable.
print "Here's your file %r:" % filename

# prints variable "txt" decimal operator is set to read the file(read)
# () with nothing in the parameters
print txt.read()

# prints "Type the filename again:" on powershell/terminal
print "Type the filename again:"
# variable named "file_again" is equal to the raw input from the end user
# parameters are set to ("> ") meaning there will be a "> " before raw input
file_again = raw_input("> ")

# variable name txt_again is equal to open the file name entered for raw input
# in the (file_again) variable
txt_again = open(file_again)

# prints what is read after opening the file from the txt_again variable
# decimal operator reads file without parameters set
print txt_again.read()

# There is no comment block ability in python, as there is java
# txt = open(filename) does not return contents of the file. It actually makes
# something called a "file object" think of a file like a dvd player.
# the dvd player is not the dvd the same way the file object is not the file's
# contents.
