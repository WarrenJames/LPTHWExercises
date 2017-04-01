# Exercise 19: Functions and Variables
# variables in functions are not connected to the variables in your script.

# def is short for define(function) which defines your Functions
# function defined is cheese_and_crackers with cheese_count
#   and boxes_of_crackers both as expressions (:) consists of printing 4 lines
# %d is a modulo for numbers/integars
def cheese_and_crackers(cheese_count, box_of crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# prints line "We can just give the function numbers directly:"
print "We can just give the function numbers directly:"
# calls function cheese_and_crackers with 20 and 30 as expressions
cheese_and_crackers(20, 30)

# prints line "OR, we can use variables from our script:"
print "OR, we can use variables from our script:"
# variable amount_of_cheese equals 10
amount_of_cheese = 10
# variable amount_of_crackers equals 50
amount_of_crackers = 50

# calls cheese_and_crackers function with amount_of_cheese and
# amount_of_crackers as expression. Almost like cheese_and_crackers(10, 50)
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints "We can even do math inside too:"
print "We can even do math inside too:"

# calls cheese_and_crackers variable with math as expressions
# Almost like cheese_and_crackers(30, 11)
cheese_and_crackers(10 + 20, 5 + 6)

# prints "And we can combine the two, variables and math:"
print "And we can combine the two, variables and math:"

# calls cheese_and_crackers with amount_of_cheese + 100
#   and amount_of_crackers + 1000 as expressions
# almost like cheese_and_crackers(10 + 100, 50 + 1000) OR
# cheese_and_crackers(110, 1050)
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
