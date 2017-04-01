# Excercise 17:
from sys import argv

from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file, 'r')

print """The input file is %d bytes long\nOutput file exists? %r\n
Read, hit RETURN to continue, CTRL-C to abort.
    """ % (len(from_file), exists(to_file))
raw_input()

out_file = open(to_file, 'w')

out_file.write(in_file)

print "Alright, all done."

out_file.close()
in_file.close()
