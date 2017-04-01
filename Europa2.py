# Europa
# Designed to improve overall happiness

from sys import argv

script, filename, filename2 = argv

good = open(filename)
bad = open(filename2)
prompt = '> '

print "Hi there my name is %s, What is yours?" % (script)
user_name = raw_input(prompt)

print "Pleased to meet you %s, how are you feeling today?" % (user_name)
print "Good or Bad?"
mood = raw_input(prompt)

if mood == ("good"):
    open("good", "w"),
print good.read()

if mood == "bad":
    with open(filename2) as b:
        b.read()
