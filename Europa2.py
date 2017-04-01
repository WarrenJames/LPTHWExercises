# Europa
# Designed to improve overall happiness

from sys import argv

script, filename, filename2 = argv

good = open(filename, 'r')
bad = open(filename2, 'r')
prompt = '> '

print "Hi there my name is %s, What is yours?" % (script)
user_name = raw_input(prompt)

print "Pleased to meet you %s, how are you feeling today?" % (user_name)
print "Good or Bad?"
mood = raw_input(prompt)

good_one = good.readline()
bad_one = bad.readline()

if mood == ("good"):
    print good_one

if mood == "bad":
    print bad_one
