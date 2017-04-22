# Boolean Operators

"""
_____________________
AND
_____________________
True and True = True
False and True = False
False and False = False
_____________________
OR
_____________________
True or True = True
True or False = True
False or False = False
_____________________
NOT
_____________________
Not True = False
Not False = True

"""

"""
_____________________
AND Examples
_____________________

"""

bool_one = 2 > 3 and -2 >= -1

bool_two = -(-(-(-2))) == -2 and 4 >= 16 **0.5

bool_three = 19 % 4 != 300 / 10 / 10 and 2 - 3 != -6 + 5

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2

bool_five = 16**2 - 32 >= 30 % 9 and 40 == 5 * 8



"""
_____________________
OR Examples
_____________________

"""
bool_six =  2**3 == 108 % 100 or 'Cheese' == 'King Arthur'

bool_seven = 5 % 4 <= 10 / 5 or 4**5 <= 20 + 10

bool_eight = 100**0.5 >= 50 or 100 % 10 >= 4

bool_nine = 16 / 4 != 2**5 or 11 <= 33 - 21

bool_ten = 1**100 == 100**1 or 3 * 2 * 1 != 3+ 2 + 1

"""
_____________________
NOT Examples
_____________________

"""

bool_eleven = not True

bool_twelve = not 3**4 < 4**3

bool_thirteen = not 10 % 3 <= 10 % 2

bool_fourteen = not 3**2 + 4**2 != 5**2

bool_fifteen = not not False

"""
Just like arithmetic operators, Booleen operators use order of
operations of their own.
not is evaluated first;
and is evaluated next;
or is evaluated last.

Parentheses ensure your expressions are evaluated in the order you want.
Anything in the parentheses is evaluated as its own unit.

"""

operations_one = False or not True and True

operations_two = False and not True or True

operations_three = True and not (False or False)

operations_four = not not True or False and not True

operations_five = False or not (True and True)





more_one = (2 <= 2) and "Alpha" == "Bravo"

more_two = (4**2 != 8) or (56 < 5**5) == True

more_three = "James" != raw_input() and 49 < 3**3

more_four = 7**7 > 7*7 != True

more_five = (not False and True) or True
