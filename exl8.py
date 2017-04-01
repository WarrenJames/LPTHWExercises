# Exercise 8: Printing, Printing

# variable is equal to "%r %r %r %r"
formatter = "%r %r %r %r"

# prints formatter modulo (modulo's value is 1, 2 ,3 ,4)
print formatter % (1, 2, 3, 4) # prints as "1 2 3 4"
# prints formatter modulo (modulo's value is "one", "two", "three", "four")
print formatter % ("one", "two", "three", "four") # prints as "one two three four"
# prints formatter modulo (modulo's value is True, False, False, True )
print formatter % (True, False, False, True) # prints as "True False False True"
# prints formatter modulo which is equal to the variable "formatter" refer to line 3
print formatter % (formatter, formatter, formatter, formatter) # prints as "%r %r %r %r"
# prints formatter modulo which is equal to line below
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
print formatter % (
    'I had this thing.',
    'That you could type right.',
    "But it didn't sing.",
    'So I said goodnight.'
)
