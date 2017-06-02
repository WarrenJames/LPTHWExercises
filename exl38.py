# Exercise 38: Doing things to Lists

import random
# creates variable with string of text "Apples Oranges Crows Telephone Light Sugar"
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# prints "Wait there are not 10 things in that list. Let's fix that."
print "Wait there are not 10 things in that list. Let's fix that."

# stuff variable is equal to ten_things variable with .split function(' ')
# Argument lets split know to split string every time it finds a space.
stuff = ten_things.split(' ')

# more_stuff is equal to list made up of:
# Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

""" while length of stuff variable is not equal to 10:
next_one variable is equal to more_stuff with .pop() function to remove first
entry.
prints "Adding: ", next_one variable ("Adding: Day")
stuff variable with .append function to append(next_one) variable to list.
prints "There are %\digit items now." %\ len of (stuff) variable
repeats until length of stuff variable is == to 10.
"""

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)


# prints "There we go: ", stuff variable
print "There we go: ", stuff

# prints "Let's do some things with stuff."
print "Let's do some things with stuff."

# prints stuff[1] spot 1 in list. or "Oranges"
print stuff[1]
# prints stuff[-1] last spot on list. or "Corn"
print stuff[-1]
# prints stuff.pop() pops the last spot on the list. Which is "Corn"
print stuff.pop()

# prints ' '.join(stuff). joins all list items using a space.
print ' '.join(stuff)
# prints '#'.join(stuff[3:5]) or joins items from stuff variable that are from
# spot 3 to (but not including) 5. or Telephone#Light
print '#'.join(stuff[3:5])


itemlist = ['alpha', 'bravo', 'charlie', 'apple']

def loopy(items):
    for i in items:
        if i[0] == 'a':
            continue
        else:
            print i

loopy(itemlist)
