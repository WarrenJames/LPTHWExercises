# Exercise 24: More practice

"""
prints on terminal as:
"Let's practice everything.
"""
print "Let's practice everything."

"""
prints on terminal as:
You'd need to know 'bout escapes with \ that do
newlines and    tabs.
"""
# Backslash is to escape characters so you do not break the code.
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

"""
poem variable is equal to string:
    The lovely world
with logic so firmly planted
cannot discern
the needs of love
nor comprehend passion from intuition
and requires an explanation

        where there is none.

"""
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# prints as: ---------------
print "---------------"
# prints poem variable
print poem
# prints as: ---------------
print "---------------"

"""
five variable is equal to:
10 - 2 + 3 - 6 or
8 + (-3) or
5
"""
five = 10 - 2 + 3 - 6

# prints as: This should be five: 5
# %s string modulo is five variable
print "This should be five: %s" % five

"""
started expression is used as a placeholder.
define function secret_formula(started): consists of
jelly_beans variable is equal to started * 500
jars variable is equal to jelly_beans variable divided by 1000
crates variable is equal to jars divided by 100
returns jelly_beans variable, jars variable, and crates variable
return makes values available to be used by python.

variables within a function are known as local variables. They can be different
outside the function (but don't have to be.)
"""
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# start_point variable is equal to 10000
start_point = 10000

"""
calls the function and fills the three variables
since function secret_formula returns 3 values, the variables could be called
anything that you want. The function just fills them in with the returns
values in the order that they are listed.
Almost like argv
"""
beans, jars, crates = secret_formula(start_point)

# prints as: With the starting point of: 10000
# %digits modulo is start_point variable
print "With a starting point of: %d" % start_point

# prints as: We'd have 5000000 beans, 5000 jars, and 50 crates
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# reassigns start_point value to equal iteself divided by 10
start_point = start_point / 10

# prints as: We can also do that this way:
print "We can also do that this way:"
# prints as: We'd have 500000 beans, 500 jars, and 5 crates.
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
