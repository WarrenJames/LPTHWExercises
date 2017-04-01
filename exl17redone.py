# Excercise 17: More files

# from system import arguement variable
from sys import argv
# from os.path import exists
# exists tests whether a path exists. Returns False for broken symbolic links
from os.path import exists

# script, from_file, and to_file are all equal to arguement variable
script, from_file, to_file = argv

# print "Copying from (string) to (string)" % interpolation formatter shows
# string 1 is from_file and string 2 is to_file
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# in_file variable is equal to open(from_file)
in_file = open(from_file)
# variable indata is equal to in_file with decimal command/method read without
# parameters ()
indata = in_file.read()

# prints "The input file is %d bytes long" %d stands for integer (decimal)
# interpolation operator(%) is equal to len(indata)
# len(object) is an integer that returns the number of items of a sequence or
# collection
print "The input file is %d bytes long" % len(indata)
# prints "Does the output file exist? %r" interpolation operator for raw string
# is exists(to_file) which checks if to_file exists. If it does, True is
# returned, if not  False is returned
print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
print "Ready, hit RETURN to continue, CTRL-C to abort."
# asks for raw input without any parameters/prompt
raw_input()
# out_file variable is equal to open to_file in write mode/method('w')
out_file = open(to_file, 'w')
# out_file with decimal operator to write indata variable
out_file.write(indata)
# print "Alright, all done."
print "Alright, all done."
# out_file.close() closes out_file in memory
# in_file.close() closes in_file in memory
out_file.close()
in_file.close()
