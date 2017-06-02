import random

def even_odd(num):
    if num % 2 is 0:
        return True
    else:
        return not num % 2

start = 5


while start != 0:
        ri = random.randint(0, 99)
        if even_odd(ri) == True:
            print "%d is even." % (ri)
        else:
            print "%d is odd." % (ri)
        start -= 1
