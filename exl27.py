# Exercise 27 Memorizing logic

# Truth Tables

#   NOT
not False # True
not True # False

#   OR
True or False # True
True or True # True
False or True # True
False or False # False

#   AND
True and False # False
True and True # True
False and True # False
False and False # False

#   NOT OR
not (True or False) # False
not (True or True) # False
not (False or True) # False
not (False or False) # True

#   NOT AND
not (True and False) # True
not (True and True) # False
not (False and True) # True
not (False and False) # True

#   != (Not equal)
1 != 0 # True
1 != 1 # False
0 != 1 # True
0 != 0 # False

#   == (Equal)
1 == 0 # False
1 == 1 # True
0 == 1 # False
0 == 0 # True

#   >= (Greater than equal)
1 >= 0 # True
1 >= 1 # True
0 >= 1 # False
0 >= 0 # True

#   <= (Less than equal)
1 <= 0 # False
1 <= 1 # True
0 <= 1 # True
0 <= 0 # True
