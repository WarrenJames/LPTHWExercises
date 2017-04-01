# Exercise 20: Functions and Files
#
# from system folder, import argument variable
from sys import argv
# script, input_file = argv
# it will look like in terminal: python exl20.py (file of choice as input_file)
script, input_file = argv

# define(function) print_all(with f as an expression): <-- consists of
# prints f.read() what is read from f(f means file) without perameters
def print_all(f):
    print f.read()

# define rewind function(with f as an expression):  <-- consists of
# f with seek command with 0 as an expression (0)
# seeks the very start of the file seeks byte 0 which is at the start of file.
def rewind(f):
    f.seek(0)

# define function print_a_line with line_count and f(file) as expressions
# consists of printing line_count, and f.readline() reads line of file without
# parameteres
def print_a_line(line_count, f):
    print line_count, f.readline()

# variable current_file is equal to open(input_file) input_file is the second
# argument variable entered in terminal (test.txt)
current_file = open(input_file)

# prints "First let's print the whole file:\n" \n means new line
print "First let's print the whole file:\n"

# calls print_all function with current_file as an expression
print_all(current_file)

# print "Now let's rewind, kind of like a tape."
print "Now let's rewind, kind of like a tape."
# calls rewind function with current_file as an expression
rewind(current_file)
# prints "Let's print three lines:" into the terminal
print "Let's print three lines:"

# variable current_line is equal to 1
# calls print_a_line function with current_line and current_file as expressions
# (1, test.txt) print_a_line prints line count as 1 while reading test.txt
current_line = 1
print_a_line(current_line, current_file)
# variable current_line is equal to current_line + 1 OR 1 + 1 OR 2
# calls function print_a_line with current_line, and current_file as expressions
# OR print_a_line(2, test.txt)
current_line = current_line + 1
print_a_line(current_line, current_file)
# variable current_line is equal to current_line + 1 OR 2 + 1 OR 3
# calls function print_a_line with current_line, and current_file as expressions
# OR print_a_line(3, test.txt)
current_line = current_line + 1
print_a_line(current_line, current_file)
# variable current_line is equal to current_line + 1 OR 3 + 1 OR 4
# calls function print_a_line with current_line, and current_file as expressions
# OR print_a_line(4, test.txt)
current_line = current_line + 1
print_a_line(current_line, current_file)

#                               TIL
# current_line variable is used more for user to keep note to know what line
# file is on. the file does not care what current_line says and will continue
## regardless. file.tell() will tell where the file head is postitioned
