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
