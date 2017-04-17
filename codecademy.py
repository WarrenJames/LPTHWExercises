# the hash sign is for comments python won't try to run as code
# A variable stores a piece of data and gives it a specific name
my_variable = 10
# A boolean is light a light switch. It can only have two values.
# can only be True or False
my_int = 7
my_float = 1.23
my_bool = True

print my_int

# You are able to change the value of variable by reassigning it
my_int = 3

print my_int

def spam():
    eggs = 12
    return eggs

print spam()

cats = True
dogs = False

# more useless variables
mysterious_variable = 42

"""Instead of using a # (hash) on each line, use triple quotes for multi-line comments
"""

# You can add, subtract, multiply, and divide numbers like this
addition = 72 + 73
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9
exponents = 10 ** 2
modulo =  11 % 5
# You can print multiple variables at a time by seperating with commas
print addition, subtraction, multiplication, division, exponents, modulo

# knowledge check: boolean, floating point, and exponents
monty = True
python = 1.234
monty_python = python ** 2

# calculate meal cost with tax and tip included
meal = 44.50
tax = 6.75 / 100 # 6.75%
tip = 15.00 / 100 # 15%

# meal is equal to itself plus 6.75% of itself.
meal = meal + meal * tax # calculate the meals cost with tip.
# total is equal to new meal mount plus 15% of itself.
total = meal + meal * tip
# prints total with floating point that has 2 digits after decimal point
print("%.2f" % total)

brian = "Hello life!"
caesar = "Graham"
praline = "John"
viking = "Teresa"

print caesar
print praline
print viking

""" Each character in a string is assigned a number. This number is called the
index. In Python we start counting the index from zero instead of one."""

fifth_letter = "Monty"[4]

print fifth_letter

# Next would be string methods, they let you preform specific tasks for strings
# string methods mentioned: len(), lower(), upper(), str()

parrot = "Norwegian Blue"
pi = 3.14
print len(parrot) # will print length of parrot string
print parrot.lower() # will print string in lower case lettering
print parrot.upper # will print string in all capital lettering
print str(pi) # turns non-strings into strings

# methods that use dot notation only work with strings
# on the other hand len() and str() work on other data types

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()
