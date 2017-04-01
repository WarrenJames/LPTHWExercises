# Europa

from sys import argv
script, user_name = argv

prompt = '> '
print "Hi there, I am %s" % (script)
print "Pleased to meet you %s" % (user_name)

print "How are you feeling today, %s?" % (user_name)
feeling = raw_input(prompt)
print "Why are you feeling %r?" % (feeling)
explain = raw_input(prompt)

print "That's interesting, when did that happen?"
time = raw_input(prompt)

print "%s? That wasn't too long ago." % (time)
