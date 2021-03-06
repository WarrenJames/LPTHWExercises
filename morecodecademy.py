# Conditional Statement Syntax

"""
'if' is a conditional statement that executes some specified code after checking
if its expression is True
"""
# define function(): which consists of
# if True: return to the user "Success #1"
def using_control_once():
    if 32 <= 4**4:
        return "Success #1"
# define function(): which consists of
# if not False: return to the user "Success #1"
def using_control_again():
    if not 50 > 5**5:
        return "Success #2"

print using_control_once()
print using_control_again()

""" An if/else pair says 'if this expression is true, run this indented code
block; otherwise, run this code after the else statement'. Unlike if, else
doesn't depend on an expression"""

"""Elif is short for 'else if' which means 'otherwise, if the following
expression is true, do this'."""

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

"""
define power(with two arguments): consists of
result variable is equal to first argument to the power of second argument
and prints "%\digit placeholder to the power of %\digit placeholder is
%\digit placeholder" %\ placeholders are (first argument, second argument,
and result variable)
"""
def power(base, exponent):
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

# calls power funtion with arguments as 37 and 4
power(37,4)
