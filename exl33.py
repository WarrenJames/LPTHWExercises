# Exercise 33: While Loops

"""
A while-loop will keep executing the code in the block under it just as long
as the boolean expression remains True.
Just like a if-statement, but instead of running the code block once,
while-loops jump back to the top where the while is, and repeat.

Rules for while-loops
1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
2. Review your while statements and make sure that the boolean test will become
false at some point.
3. When in doubt print out your test variable at the top and bottom of the
while-loop to see what it's doing.
"""


numbers = []

def wloop(i):
    h = 11
    while i < h:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


wloop(1)

print "The numbers: "

for num in numbers:
    print num
