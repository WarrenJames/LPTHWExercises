# Exercise 30: Else and If

# people variable is equal to 30
people = 30
# cars variable is equal to 40
cars = 40
# trucks variable is equal to 15
trucks = 15

""" If cars variable is greater than people variable(True), print onto terminal:
'We should take the cars'
else if cars variable is less than people variable(False), print onto terminal:
'We should not take the cars'
else, print onto terminal 'we can't decide' """
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

""" if trucks variable is greater than cars variable(False), print onto
terminal: 'That's too many trucks.
else if trucks variable is less than cars variable(True), print onto terminal:
'Maybe we could take the trucks.'
else, print onto terminal 'We still can't decide.' """
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

""" If people variable is greater than trucks variable(True), print onto
terminal: 'Alright, let's just take the trucks.'
else print onto terminal: 'Fine, let's stay home then."""
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

""" If cars variable is greater than people variable(True) or trucks variable
is less than cars variable(True), print onto terminal: 'We're taking a car.' """
if cars > people or trucks < cars:
    print "We're taking a car."  
