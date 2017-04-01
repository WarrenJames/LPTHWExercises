# Excercise 16 reader

# from system, import arguement variable
from sys import argv
# script, and filename are first and second argument variables
script, filename = argv
# reader variable is open(filename) filename is second argument variable
reader = open(filename)
# prints reader variable with decimal operator, read method with no parameters
print reader.read()

# closes readers file in memory
reader.close
