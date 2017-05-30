# ----- and -----

"""
and, or, not are logical operators. and will result into True only if both the
operands are True.

Examples:
"""

True and True # True
True and False # False
False and True # False
False and False # False

# ----- as -----
"""
as is used to create an alias while importing a module. It means giving a
different name (user-defined) to a module while importing it.

Examples:
"""

import turtle as franklin # <-- made up alias

turt = franklin.Turtle()
turt.forward(200)




franklin.done()

# ----- assert -----

"""
assert is used for debugging purposes.

While programming, sometimes we wish to know the internal state or
check if our assumptions are true. assert helps us do this and find
bugs more conveniently. assert is followed by a condition.
If the condition is true, nothing happens. But if the condition is
false, AssertionError is raised.

Examples:
"""
tw = 12000

# assert tw > 20000, "Not bigger than 20k."
# assert 4 > 5, "Number is too small."

# ----- break -----

"""
break (and continue) is used inside for and while loops to alter their normal
behavior. It will end the smallest loop it is in and control flows to the
statement below the loop.

Examples:
"""

for i in range(1, 11): # loop intends to print numbers from 1 to 10
    if i == 6: # but if the if condition is met when i is equal to 6:
        break # we break from the loop
    print i # and the loop only prints numbers 1 through 5

# ----- class -----

"""
class is used to define a new user-defined class in Python.

Class is a collection of related attributes and methods that try to represent
a real world situation. This idea of putting data and functions together in a
class is central to the concept of object-oriented programming(OOP).

Classes can be defined anywhere in a program. But it is a good practice to
define a single class in a module.

Always capitalize first letter of class name.
way of packaging variables and functions together.

Examples:
"""

class ExampleClass:
    def function():
        print apple
    def function2():
        print pie

# called like a module as ExampleClass.function()

# ----- continue -----

"""
continue (and break) is used inside for and while loops to alter their normal
behavior. It will skip the iteration and continue with the loop.

Examples:
"""
for i in range(1, 11): # loop intends to print numbers from 1 to 10
    if i == 6: # but if the if condition is met when i is equal to 6:
        continue # we will skip the iteration and continue
    print i # and the loop prints numbers 1 through 5, skips 6,
            # and continues printing numbers 7 through 10.

# ----- def -----

"""
def is used to define a a user-defined function.
a Function is a block of rlated statements, which together does some specific
task. It helps organize code into manageable chunks and also to do some
repetative tasks.

Examples:
"""
def multiply(a, b):
    return a * b

# called as:
multiply(1, 10)

# ---- del ----

"""
del is used to delete the reference to an object.
Everything is an object in Python.

Examples:
"""

delvar = 10
dellist = ['1', '2', '3', '4', '5']

del delvar # deletes the variable delvar
del dellist[3:6] # deletes items in a list in places 1 and stops at 6


for i in dellist: # for-loop will only print numbers 1, 2, 3
    print i

# ----- elif -----

"""
elif is used along with if, and else for conditional branching or decision making

When we want to test a condition and execute a block only if the condition is true,
then we use if and elif. elif is short for 'ELSE IF'.


Examples:
"""

def elifEx(a):
    if a == 1:
        print "One"
    elif a == 2:
        print "Two"
    elif a == 3:
        print "Three"
    else:
        print "Different number entered"

elifEx(2)

# ----- else -----

"""

else is the block which is executed if the condition is false.

Examples:
"""

def elEx():

    a = raw_input("> ")
    if a == "Sith":
        print "You have joined the Darkside."
    else:
        print "Traitor!"

print "Jedi or Sith?"

elEx()

# ----- except -----

"""
except, raise, try are used with exceptions in Python.

Exceptions are basically errors that suggests something went wrong while
executing our program. IOError, ValueError, ZeroDivisionError, ImportError,
NameError, TypeError etc. are a few examples of exception in Python.
try...except blocks are used to catch exceptions in Python.

We can raise an exception explicitly with the raise keyword.

Examples:
"""

def recip(num):
    try:
        r = 100 / num
    except:
        print "Exception Caught"
        return
    return r

print recip(10) # function will divide r (which equals 100) and print "10"
print recip(0) # function will raise ZeroDivisionError and print exception

# ----- exec -----

"""

"""

# ----- finally -----

"""
finally is used with try...except blocks to close up resources or file streams.
Using finally ensures that the block of code inside it gets executed even if
there is an unhandled exception.

Exceptions or not, finally do this no matter what.

Examples:
"""

try:
    x = str(5) + " strings."
except ZeroDivisionError:
    print "Will appear if finding Zero Division Error"
finally:
    print "finally prints before error code prints."

# ----- for -----
"""
for is used for looping. Generally we use for when we know the numbers of times
we want to loop. In python we can use it with any type of sequence like a list
or a string.


Examples:
"""

names = ['James', 'Paul', 'Gary', 'Isabel', 'Angelica']

for i in names:
    print "Hello " + i

# ----- from -----

"""
imports specific parts of a module into the script.

Examples:
"""

import math
# will import the math module. Now we can use the cos() function inside it as
print math.cos(2)
# but if we wanted to import just the cos() function this can be done like:
from math import cos

print cos(2)

# ----- global -----

"""
global is used to declare that a variable inside the function is global
(outside of function). If we need to read the value of a global variable, it is
not necessary to fine it as a global.  This is understood.

If we need to modify the value of a global variable inside a function, then
we must declare it with global. Otherwise a local variable with that name is
created.

Examples:
"""

globVar = 10
def read1():
    print globVar

# will not modify globVar global variable. local variable with that name is
# created instead.
def write1():
    globVar = 15

# correct way to modify global variable in function:
def write2():
    global globVar
    globVar = 5

# ----- if -----

"""
if, else and elif are used for conditional branching or decision making.
When we want to test some condition and execute a block only if the condition
is true, then we use if and elif. elif is short for else if. else is the block
which is executed if the condition is false.

Examples:
"""
def ifExample(a):
    if a == 1:
        print "One"
    elif a == 2:
        print "Two"
    else:
        print "Other number."

ifExample(1)
ifExample(2)
ifExample(10  )


# ----- not -----

"""
not operator is used to invert the truth value.

Examples:
"""

not True # False
not False # True

# ----- or -----

"""
or will result into True if any of the operands is True.

Examples:
"""

True or True # True
True or False # True
False or True # True
False or False # False
