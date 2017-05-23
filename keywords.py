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
