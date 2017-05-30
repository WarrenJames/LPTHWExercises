# Drill

# variables/lists
rgb = ['Red', 'Green', 'Blue']
fruits = ['Bananas', 'Grapes', 'Strawberries', 'Raspberries']
num = 1
racestart = 4

# for-loops
for color in rgb:
    print color

for fruit in fruits:
    print "A type of fruit that I enjoy is: %s" % fruit

# while-loops
while num <= 3:
    print "Number now equals:", num
    num += 1

while racestart > 0:
    print "%d!" % racestart
    racestart -= 1

# functions
def div(a, b):
    print "%d / %d is equal to:" % (a, b), a / b

div(50, 10)

def multi(a, b):
    print "%d * %d is equal to:" % (a, b)
    return a * b

print multi(10, 5)
