import os

# shopping_list variable is equal to empty list.
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

""" define function show(takes no arguments): consists of

printing "Shopping list consist of:" onto terminal
for each item in shopping_list:
    for loop will print item
"""
def show():
    print "Shopping list consists of:"
    index = 1
    for i in shopping_list:
        print "%s %s"% (index, i)
        index += 1
    print "_" * 10
"""
define function help(takes no arguments) consists of:
printing "What should we pick up at the store?" onto terminal
and printing
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see current list.
Enter 'HELP' to view help.
onto terminal

"""

def help():
    clear_screen()
    print "What should we pick up at the store?"
    print """
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see current list.
Enter 'HELP' to view help."""

"""
define function add(takes one argument) consists of:
shopping_list variable being appended with a dot operator(argument taken)
prints "added %\string modulo to the list, List now contains %\digit modulo items."
modulos are equal to item, and length of (shopping_list)
"""
def add(item):
    clear_screen()
    shopping_list.append(item)
    print "Added %s to the list, List now contains %d items." % (item, len(shopping_list))
    show()
"""
define function main(takes no arguments) consists of:
calling help() function
while True: (infinite while-loop)
    item variable is equal to raw_input("> as prompt")
    if item variable is equal to "DONE": then
    break
else if item variable is equal to "SHOW": then
call show() function
and then continue
else if item is equal to "HELP" then
call help() function
and then continue
else:
    call add function with input from (item) as argument

calls show() function

"""
def main():
    help()

    while True:
        item = raw_input("> ")
        if item.upper() == "DONE" or item.upper() == "QUIT":
            break
        elif item.upper() == "SHOW":
            show()
            continue
        elif item.upper() == "HELP":
            help()
            continue
        else:
            add(item)

    show()

# calls main function to start game
main()
